"""
Author: Shubham Darda
Description: Helper script to prepare and run the GoDarda application (Jekyll-based site) locally.

Notes (production, documentation-only changes and small robustness fixes):
- Purpose: detect environment, perform a lightweight or "full" setup for local Jekyll development,
  and start or build the site. Designed to be run from the repository root or from any folder
  (the script will cd into the repository when appropriate).
- Modes:
  - light (default): perform minimal checks and attempt to start the Jekyll server.
  - full: install system packages, Python test requirements and Ruby gems (bundler), optionally
    clone the repository if missing, cleanup ignored files, then build/serve the site.
- Platforms:
  - Optimized for Ubuntu Linux (uses apt/snap where appropriate).
  - Supports Windows 11+ (no mandatory sudo requirement).
  - GitHub Actions CI: reduced package list and build-only behavior.
- Safety / robustness improvements in this version:
  - Consolidated command runner with captured output and robust exception handling.
  - All public functions/methods use try/except to avoid uncontrolled crashes.
  - Starting server streams console output.
- How to run:
  - Light: python setup.py
  - Full:  python setup.py full
"""

from __future__ import annotations

import os
import platform
import socket
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Sequence

# --- configuration / constants ---
REPO_DIRNAME = "godarda.github.io"
DEFAULT_JEKYLL_PORT = 4000
MIN_FREE_GIB = 2

# --- helpers -----------------------------------------------------------------
def run_cmd(cmd: Sequence[str] | str, *, shell: bool = False, check: bool = False, timeout: int | None = None) -> subprocess.CompletedProcess | None:
    """
    Run a command and return CompletedProcess. Returns None on unexpected exception.
    - Use shell=True for single-string commands that require shell features.
    - Captures stdout/stderr to CompletedProcess.stdout for debugging on failure.
    """
    try:
        if isinstance(cmd, str) and not shell:
            cmd = cmd.split()
        return subprocess.run(cmd, check=check, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=timeout)
    except subprocess.CalledProcessError as e:
        return e
    except Exception:
        return None

def _run_cmd_stream(cmd: str, shell: bool = True) -> int:
    """
    Run a long-running command and stream stdout/stderr to the console.
    Returns the process returncode; returns non-zero on start failure.
    """
    try:
        proc = subprocess.Popen(cmd if shell else cmd.split(),
                                shell=shell,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                text=True,
                                bufsize=1)
    except Exception:
        return 1
    try:
        if proc.stdout:
            for line in proc.stdout:
                print(line.rstrip())
        proc.wait()
        return proc.returncode if proc.returncode is not None else 1
    except KeyboardInterrupt:
        try:
            proc.terminate()
        except Exception:
            pass
        raise
    except Exception:
        try:
            proc.terminate()
        except Exception:
            pass
        return 1

def safe_rmtree(path: str) -> None:
    try:
        shutil.rmtree(path, ignore_errors=True)
    except Exception:
        pass

def free_disk_gib(path: Path) -> int:
    try:
        total, used, free = shutil.disk_usage(str(path))
        return free // (2 ** 30)
    except Exception:
        return 0

def is_command_available(name: str) -> bool:
    try:
        return shutil.which(name) is not None
    except Exception:
        return False

def windows_build_number() -> int:
    """Return Windows build number (0 when not available)."""
    try:
        if hasattr(sys, "getwindowsversion"):
            return int(sys.getwindowsversion().build)
        parts = platform.version().split(".")
        if len(parts) >= 3:
            return int(parts[2])
    except Exception:
        pass
    return 0

def connected_to_internet(timeout: float = 2.0) -> bool:
    try:
        with socket.create_connection(("8.8.8.8", 53), timeout=timeout):
            return True
    except Exception:
        return False

def _print_progress(pct: int, msg: str | None = None) -> None:
    try:
        msg = msg or ""
        print(f"[{pct:3d}%] {msg}", flush=True)
    except Exception:
        pass

# progress helpers: monotonic snapping to 1, multiples of 5, then 100
_PROGRESS_LAST = -1

def _snap_to_step(pct: int) -> int:
    if pct <= 1:
        return 1
    if pct >= 100:
        return 100
    return ((pct + 4) // 5) * 5

def _show_progress(pct: int, msg: str | None = None) -> None:
    global _PROGRESS_LAST
    try:
        snap = _snap_to_step(pct)
        if snap > _PROGRESS_LAST:
            _PROGRESS_LAST = snap
            _print_progress(snap, msg)
    except Exception:
        pass

# --- core logic --------------------------------------------------------------
class Setup:
    def __init__(self, repo_root: Path, ubuntu: bool = False, github_actions: bool = False, windows: bool = False):
        self.repo_root = repo_root
        self.ubuntu = ubuntu
        self.github_actions = github_actions
        self.windows = windows
        self.cwd = Path.cwd()
        self.free_gib = free_disk_gib(self.cwd)

    def _ensure_in_repo(self) -> None:
        try:
            if REPO_DIRNAME not in str(Path.cwd().name) and (self.repo_root.name == REPO_DIRNAME or REPO_DIRNAME in str(self.cwd)):
                os.chdir(str(self.repo_root))
        except Exception:
            pass

    def _print_versions(self) -> None:
        cmds = ("ruby -v", "gem -v", "bundle exec jekyll -v", "bundler -v")
        for cmd in cmds:
            try:
                out = run_cmd(cmd, shell=True)
                if out and out.stdout:
                    print(out.stdout.strip())
            except Exception:
                print(f"(unable to run: {cmd})")

    def install_packages(self) -> None:
        """Install packages and project dependencies. Best-effort; exits on unrecoverable bundle install failure."""
        try:
            _show_progress(1, "Starting installation sequence")

            packages = ""
            if self.ubuntu:
                _show_progress(5, "Updating package lists")
                run_cmd("sudo apt-get update -y", shell=True)

                _show_progress(10, "Upgrading system packages")
                run_cmd("sudo apt-get full-upgrade -y", shell=True)

                if self.github_actions:
                    packages = "ruby-full clisp rustc freeglut3-dev nasm shc"
                else:
                    packages = (
                        "python3-pip git-all openjdk-21-jre openjdk-21-jdk ruby-full build-essential "
                        "zlib1g-dev dotnet-sdk-8.0 r-base octave clisp maxima rustc freeglut3-dev "
                        "mysql-server nasm nmap shc finger"
                    )

                    # optional snaps (best-effort)
                    if is_command_available("snap"):
                        if not is_command_available("code"):
                            run_cmd("sudo snap install --classic code", shell=True)
                        if not is_command_available("julia"):
                            run_cmd("sudo snap install julia --classic", shell=True)

                if packages:
                    _show_progress(15, "Installing system packages")
                    # bulk install with minimal overhead (time complexity: O(n) packages)
                    for pkg in packages.split():
                        try:
                            run_cmd(f"sudo apt-get -y --ignore-missing install {pkg}", shell=True)
                        except Exception:
                            pass
                    _show_progress(30, "System packages installation complete")

                if not self.github_actions and REPO_DIRNAME not in str(Path.cwd()):
                    run_cmd(f"git clone https://github.com/godarda/godarda.github.io.git", shell=True)
                    try:
                        os.chdir(str(self.repo_root))
                    except Exception:
                        pass

            # Ensure repository context
            self._ensure_in_repo()

            _show_progress(50, "Installing Python test requirements")
            # Inform user this step may take time (pip downloads/builds)
            run_cmd("pip install --user --upgrade -r tests/requirements.txt --break-system-packages --no-warn-script-location", shell=True)

            # Bundler / gems
            try:
                # ensure repo context for bundler commands (important on Windows)
                self._ensure_in_repo()

                sudo_prefix = "sudo " if (is_command_available("sudo") and (self.ubuntu or self.windows)) else ""
                gem_install_cmd = f"{sudo_prefix}gem install bundler"

                # run gem install in repo context; capture output and timeout to avoid hangs
                gi = subprocess.run(
                    gem_install_cmd,
                    shell=True,
                    cwd=str(self.repo_root),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    timeout=300,
                )
                if gi.returncode != 0:
                    # warn and continue (bundler may already be present)
                    print("Warning: 'gem install bundler' returned non-zero. Continuing if bundler exists.")
                    if gi.stdout:
                        print(gi.stdout)

                # Instead of running `bundle config` (sometimes interactive / hangs on Windows),
                # set BUNDLE_PATH in the environment and ensure vendor/bundle exists.
                _show_progress(70, "Configuring bundler (non-interactive)")
                bundle_env = os.environ.copy()
                vendor_dir = Path(self.repo_root) / "vendor" / "bundle"
                try:
                    vendor_dir.mkdir(parents=True, exist_ok=True)
                except Exception:
                    pass
                bundle_env["BUNDLE_PATH"] = str(vendor_dir)

                _show_progress(80, "Installing Ruby gems (this may take several minutes)")
                bundle_cmd = "bundle install --path vendor/bundle --jobs=4 --retry=3 --no-color"
                bi = subprocess.run(
                    bundle_cmd,
                    shell=True,
                    cwd=str(self.repo_root),
                    env=bundle_env,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    timeout=1800,
                )
                if bi.returncode != 0:
                    _show_progress(95, "Ruby gem installation failed")
                    if bi.stdout:
                        print(bi.stdout)
                    sys.exit(1)

                _show_progress(100, "Ruby gems installed")
            except subprocess.TimeoutExpired as e:
                print("Timeout during bundler/gem step:", str(e))
                sys.exit(1)
            except Exception as e:
                print("Error during bundler/gem step:", str(e))
                sys.exit(1)
        except Exception:
            # defensive catch-all: print a short hint and re-raise only if critical
            print("An unexpected error occurred during installation. Try running with 'full' again or inspect earlier output.")
            raise

    def start_server(self) -> None:
        """Start or build the Jekyll site.

        - CI: perform build and return.
        - Local: require bundle and satisfied project gems; stream server output to console.
        - Do not use sudo for running the server (avoids environment issues).
        """
        try:
            self._ensure_in_repo()

            print("-" * 45)
            print("The following versions are getting used")
            print("-" * 45)
            self._print_versions()
            print("-" * 45)

            if self.github_actions:
                print("Building site (CI)...")
                out = run_cmd("bundle exec jekyll build", shell=True, timeout=600)
                if out and out.returncode == 0:
                    print("Build completed.")
                    return
                print("Build failed:")
                if out and out.stdout:
                    print(out.stdout)
                sys.exit(1)

            # Local serve: check tools and gems
            if not is_command_available("bundle"):
                print("Required tool 'bundle' not found in PATH. Run 'python setup.py full' to install dependencies.")
                sys.exit(1)

            check = run_cmd("bundle check", shell=True)
            if not check or getattr(check, "returncode", 1) != 0:
                print("Project gems are not satisfied. Run 'python setup.py full' or 'bundle install --path vendor/bundle'.")
                if check and getattr(check, "stdout", None):
                    print(check.stdout.strip())
                sys.exit(1)

            cmd = f"bundle exec jekyll serve --host 127.0.0.1 --port {DEFAULT_JEKYLL_PORT}"
            print("Starting Jekyll server...")
            # stream logs; blocking call until server stops
            rc = _run_cmd_stream(cmd, shell=True)
            if rc != 0:
                print("Jekyll server exited with non-zero status.")
                sys.exit(rc)
        except KeyboardInterrupt:
            pass
        except Exception as exc:
            print("Unable to start the Jekyll server:", str(exc))
            sys.exit(1)

    def clean_ignored(self) -> None:
        try:
            igf = Path(self.repo_root) / ".gitignore"
            if igf.exists():
                for line in igf.read_text().splitlines():
                    p = line.strip()
                    if p and not p.startswith("#"):
                        safe_rmtree(p)
                if self.ubuntu:
                    run_cmd("sudo rm -rf _site/", shell=True)
        except Exception:
            pass

    def run_full(self) -> None:
        try:
            if self.free_gib < MIN_FREE_GIB:
                print(f"Insufficient disk space. Required {MIN_FREE_GIB} GiB or more for full setup.")
                return

            if Path.cwd().name == REPO_DIRNAME:
                self.clean_ignored()

            if self.ubuntu:
                self.install_packages()
                run_cmd("sudo apt-get clean -y", shell=True)
                run_cmd("sudo apt-get autoclean -y", shell=True)
                run_cmd("sudo apt-get autoremove -y", shell=True)
            else:
                self.install_packages()

            self.start_server()
        except Exception:
            print("Full setup failed. See prior messages for details.")
            raise

    def run_light(self) -> None:
        try:
            self.start_server()
        except Exception:
            print("Light setup failed. See prior messages for details.")
            raise

# --- entry point -------------------------------------------------------------
def main() -> None:
    try:
        if sys.version_info < (3, 4):
            print("Python 3.4 or later is needed for setup.")
            return

        cwd = Path.cwd()
        repo_root = cwd
        if cwd.name != REPO_DIRNAME:
            candidate = cwd / REPO_DIRNAME
            if candidate.exists():
                repo_root = candidate

        is_ubuntu = False
        is_github_actions = os.getenv("GITHUB_ACTIONS") == "true"
        is_windows_supported = False

        if sys.platform == "linux":
            try:
                env_id = platform.freedesktop_os_release().get("ID", "").lower()
            except Exception:
                env_id = ""
            try:
                run_cmd(f"sudo kill -9 $(sudo lsof -t -i:{DEFAULT_JEKYLL_PORT}) 2>/dev/null", shell=True)
            except Exception:
                pass
            if env_id == "ubuntu":
                is_ubuntu = True
            else:
                if env_id:
                    print("Note: script is optimized for Ubuntu Linux. Proceeding with best-effort behavior.")
        elif sys.platform == "win32":
            build = windows_build_number()
            if build >= 22000:
                is_windows_supported = True
            else:
                print("Unsupported Windows version. This script supports Windows 11 (build >= 22000) only.")
                return
        else:
            print("Setup only works on Windows and Ubuntu OS (best-effort for other Linux).")
            return

        s = Setup(repo_root=repo_root, ubuntu=is_ubuntu, github_actions=is_github_actions, windows=is_windows_supported)

        full = False
        if len(sys.argv) > 1 and sys.argv[1].lstrip("-").lower() == "full":
            full = True

        if connected_to_internet():
            if full:
                s.run_full()
            else:
                s.run_light()
        else:
            if full:
                print("A full setup requires an internet connection. You may continue without the full option.")
            else:
                s.run_light()
    except Exception:
        print("Fatal error in setup. See above messages for details.")
        raise

if __name__ == "__main__":
    main()
# This script is intended to be run as a standalone program.