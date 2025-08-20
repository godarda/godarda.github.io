"""
Author: Shubham Darda
Description: Helper script to prepare and run the GoDarda application (Jekyll-based site) locally.

Notes (production, documentation-only changes and small robustness fixes):
- Purpose: detect environment, perform a lite or "full" setup for local Jekyll development,
  and start or build the site. Designed to be run from the repository root or from any folder
  (the script will cd into the repository when appropriate).
- Modes:
  - Lite (default): perform minimal checks and attempt to start the Jekyll server.
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
  - Lite: python setup.py
  - Full: python setup.py full
"""

from __future__ import annotations

import logging
import os
import platform
import socket
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Sequence

# configure console logging (DEBUG and above)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

# --- configuration / constants ---
REPO_DIRNAME = "godarda.github.io"
DEFAULT_JEKYLL_PORT = 4000
MIN_FREE_GIB = 2


# --- helpers -----------------------------------------------------------------
def run_cmd(
    cmd: Sequence[str] | str, *, shell: bool = False, check: bool = False, timeout: int | None = None
) -> subprocess.CompletedProcess | None:
    """
    Run a command and return CompletedProcess. Returns None on unexpected exception.
    - Use shell=True for single-string commands that require shell features.
    - Captures stdout/stderr to CompletedProcess.stdout for debugging on failure.
    """
    try:
        if isinstance(cmd, str) and not shell:
            cmd = cmd.split()
        return subprocess.run(
            cmd,
            check=check,
            shell=shell,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=timeout,
        )
    except subprocess.CalledProcessError as e:
        # Return the CalledProcessError object (kept behavior)
        return e
    except Exception as e:
        logger.debug("run_cmd unexpected error for %r: %s", cmd, e)
        return None


def run_cmd_stream(cmd: str, shell: bool = True) -> int:
    """
    Run a long-running command and stream stdout/stderr to the console.
    Returns the process returncode; returns non-zero on start failure.
    """
    try:
        proc = subprocess.Popen(
            cmd if shell else cmd.split(),
            shell=shell,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
    except Exception as e:
        logger.error("Failed to start command %r: %s", cmd, e)
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
        except Exception as e:
            logger.debug("Failed to terminate process after KeyboardInterrupt: %s", e)
        raise
    except Exception as e:
        try:
            proc.terminate()
        except Exception as e2:
            logger.debug("Failed to terminate process after exception: %s", e2)
        logger.exception("Streaming command failed: %s", cmd)
        return 1


def safe_rmtree(path: str) -> None:
    try:
        shutil.rmtree(path, ignore_errors=True)
    except Exception as e:
        logger.warning("safe_rmtree failed for %r: %s", path, e)


def get_free_disk_gib(path: Path) -> int:
    """
    Returns the free disk space at the given path in GiB.
    Logs a debug message and returns 0 on failure.
    """
    try:
        free = shutil.disk_usage(path).free
        return free >> 30  # Convert bytes to GiB using bitwise shift
    except Exception as e:
        logger.debug("Failed to retrieve free disk space for path '%s'. Exception: %s", path, e)
        return 0



def command_exists(name: str) -> bool:
    try:
        return shutil.which(name) is not None
    except Exception as e:
        logger.debug("command_exists check failed for %r: %s", name, e)
        return False


def windows_build_number() -> int:
    # Return Windows build number (0 when not available)
    try:
        if hasattr(sys, "getwindowsversion"):
            return int(sys.getwindowsversion().build)
        parts = platform.version().split(".")
        if len(parts) >= 3:
            return int(parts[2])
    except Exception as e:
        logger.debug("windows_build_number failed: %s", e)
    return 0


def has_internet_connection(timeout: float = 2.0) -> bool:
    try:
        with socket.create_connection(("8.8.8.8", 53), timeout=timeout):
            return True
    except Exception as e:
        logger.debug("Internet connectivity check failed: %s", e)
        return False


def print_progress(pct: int, msg: str | None = None) -> None:
    try:
        msg = msg or ""
        print(f"[{pct:3d}%] {msg}", flush=True)
    except Exception as e:
        logger.debug("print_progress failed: %s", e)


# progress helpers: monotonic snapping to 1, multiples of 5, till 100
_PROGRESS_LAST = -1


def snap_to_step(pct: int) -> int:
    if pct <= 1:
        return 1
    if pct >= 100:
        return 100
    return ((pct + 4) // 5) * 5


def show_progress(pct: int, msg: str | None = None) -> None:
    """
    Show progress, snapping to 1%, then multiples of 5, till 100.
    """
    global _PROGRESS_LAST
    try:
        snap = snap_to_step(pct)
        if snap > _PROGRESS_LAST:
            _PROGRESS_LAST = snap
            print_progress(snap, msg)
    except Exception as e:
        logger.debug("show_progress failed: %s", e)


# --- core logic --------------------------------------------------------------
class Setup:
    def __init__(self, repo_root: Path, ubuntu: bool = False, github_actions: bool = False, windows: bool = False):
        self.repo_root = repo_root
        self.ubuntu = ubuntu
        self.github_actions = github_actions
        self.windows = windows
        self.cwd = Path.cwd()
        self.free_gib = get_free_disk_gib(self.cwd)

    def ensure_in_repo(self) -> None:
        try:
            if REPO_DIRNAME not in str(Path.cwd().name) and (
                self.repo_root.name == REPO_DIRNAME or REPO_DIRNAME in str(self.cwd)
            ):
                os.chdir(str(self.repo_root))
                logger.debug("Changed working directory to repo: %s", self.repo_root)
        except Exception as e:
            logger.warning("ensure_in_repo failed: %s", e)

    def print_versions(self) -> None:
        cmds = ("ruby -v", "gem -v", "bundle exec jekyll -v", "bundler -v")
        for cmd in cmds:
            try:
                out = run_cmd(cmd, shell=True)
                if out and getattr(out, "stdout", None):
                    print(out.stdout.strip())
            except Exception:
                logger.debug("Unable to run: %s", cmd)

    def install_packages(self) -> None:
        """Install packages and project dependencies. Best-effort; exits on unrecoverable bundle install failure."""
        try:
            show_progress(1, "Starting installation sequence")

            packages = ""
            if self.ubuntu:
                show_progress(5, "Updating package lists")
                run_cmd("sudo apt-get update -y", shell=True)

                show_progress(10, "Upgrading system packages")
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
                    if command_exists("snap"):
                        if not command_exists("code"):
                            run_cmd("sudo snap install --classic code", shell=True)
                        if not command_exists("julia"):
                            run_cmd("sudo snap install julia --classic", shell=True)

                if packages:
                    show_progress(15, "Installing system packages")
                    for pkg in packages.split():
                        try:
                            run_cmd(f"sudo apt-get -y --ignore-missing install {pkg}", shell=True)
                        except Exception as e:
                            logger.warning("Failed to install package %s: %s", pkg, e)
                    show_progress(30, "System packages installation complete")

                if not self.github_actions and REPO_DIRNAME not in str(Path.cwd()):
                    try:
                        run_cmd("git clone https://github.com/godarda/godarda.github.io.git", shell=True)
                    except Exception as e:
                        logger.warning("git clone failed: %s", e)
                    try:
                        os.chdir(str(self.repo_root))
                    except Exception as e:
                        logger.warning("chdir to repo after clone failed: %s", e)

            # Ensure repository context
            self.ensure_in_repo()

            show_progress(50, "Installing Python test requirements")
            run_cmd("pip install --user --upgrade -r tests/requirements.txt --break-system-packages --no-warn-script-location", shell=True)

            # Bundler / gems
            try:
                self.ensure_in_repo()
                sudo_prefix = "sudo " if (command_exists("sudo") and (self.ubuntu or self.windows)) else ""
                gem_install_cmd = f"{sudo_prefix}gem install bundler"

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
                    logger.warning("'gem install bundler' returned non-zero. Continuing if bundler exists.")
                    if getattr(gi, "stdout", None):
                        logger.debug(gi.stdout)

                show_progress(70, "Configuring bundler (non-interactive)")
                bundle_env = os.environ.copy()
                vendor_dir = Path(self.repo_root) / "vendor" / "bundle"
                try:
                    vendor_dir.mkdir(parents=True, exist_ok=True)
                except Exception as e:
                    logger.warning("Failed to create vendor dir %s: %s", vendor_dir, e)
                bundle_env["BUNDLE_PATH"] = str(vendor_dir)

                show_progress(80, "Installing Ruby gems (this may take several minutes)")
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
                    show_progress(95, "Ruby gem installation failed")
                    if getattr(bi, "stdout", None):
                        logger.debug(bi.stdout)
                    logger.error("Bundler install failed. Exiting.")
                    sys.exit(1)

                show_progress(100, "Ruby gems installed")
            except subprocess.TimeoutExpired as e:
                logger.exception("Timeout during bundler/gem step: %s", e)
                sys.exit(1)
            except Exception as e:
                logger.exception("Error during bundler/gem step: %s", e)
                sys.exit(1)
        except Exception as e:
            logger.exception("An unexpected error occurred during installation: %s", e)
            raise

    def start_server(self) -> None:
        """Start or build the Jekyll site.
        - CI: perform build and return.
        - Local: require bundle and satisfied project gems; stream server output to console.
        - Do not use sudo for running the server (avoids environment issues).
        """
        try:
            self.ensure_in_repo()

            # Pre-check in lite (non-CI) mode: give single-line exit when missing
            if not self.github_actions:
                if not command_exists("bundle"):
                    print("Required tool 'bundle' not found in PATH. Run 'python setup.py full' to install dependencies.")
                    sys.exit(1)

                check = run_cmd("bundle check", shell=True)
                if not check or getattr(check, "returncode", 1) != 0:
                    print("Project gems are not satisfied. Run 'python setup.py full' or 'bundle install --path vendor/bundle'.")
                    sys.exit(1)

            print("-" * 45)
            print("The following versions are getting used")
            print("-" * 45)
            self.print_versions()
            print("-" * 45)

            if self.github_actions:
                print("Building site (CI)...")
                out = run_cmd("bundle exec jekyll build", shell=True, timeout=600)
                if out and getattr(out, "returncode", 1) == 0:
                    print("Build completed.")
                    return
                logger.error("Build failed.")
                if out and getattr(out, "stdout", None):
                    logger.debug(out.stdout)
                sys.exit(1)

            # Local serve (pre-check passed)
            cmd = f"bundle exec jekyll serve --host 127.0.0.1 --port {DEFAULT_JEKYLL_PORT}"
            print("Starting Jekyll server...")
            rc = run_cmd_stream(cmd, shell=True)
            if rc != 0:
                logger.error("Jekyll server exited with non-zero status.")
                sys.exit(rc)
        except KeyboardInterrupt:
            pass
        except Exception as exc:
            logger.exception("Unable to start the Jekyll server: %s", exc)
            print("Unable to start the Jekyll server:", str(exc))
            sys.exit(1)

    def clean_ignored(self) -> None:
        """
        Removes paths listed in .gitignore and optionally clears _site/ on Ubuntu.
        Logs a warning if any step fails.
        """
        try:
            gitignore_path = Path(self.repo_root) / ".gitignore"
            if not gitignore_path.exists():
                return
            for line in gitignore_path.read_text().splitlines():
                path = line.strip()
                if path and not path.startswith("#"):
                    safe_rmtree(path)
            if self.ubuntu:
                run_cmd("sudo rm -rf _site/", shell=True)
        except Exception as e:
            logger.warning(f"Failed to process .gitignore: {e}")


    def full_setup(self) -> None:
        """
        Performs the full setup process:
        - Checks disk space
        - Cleans ignored files if in repo root
        - Installs packages and runs cleanup (Ubuntu only)
        - Starts the server
        """
        try:
            if self.free_gib < MIN_FREE_GIB:
                logger.error(f"[Setup] Insufficient disk space: {self.free_gib} GiB available, "
                             f"{MIN_FREE_GIB} GiB required.")
                return

            if Path.cwd().name == REPO_DIRNAME:
                self.clean_ignored()

            self.install_packages()

            if self.ubuntu:
                for cmd in [
                    "sudo apt-get clean -y",
                    "sudo apt-get autoclean -y",
                    "sudo apt-get autoremove -y"
                ]:
                    run_cmd(cmd, shell=True)

            self.start_server()

        except Exception as e:
            logger.exception("Full setup failed.")
            raise


# --- entry point -------------------------------------------------------------
def main() -> None:
    try:
        if sys.version_info < (3, 4):
            logger.error("Python 3.4 or later is needed for setup.")
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
            except Exception as e:
                logger.debug("Could not read freedesktop os release: %s", e)
                env_id = ""
            try:
                run_cmd(f"sudo kill -9 $(sudo lsof -t -i:{DEFAULT_JEKYLL_PORT}) 2>/dev/null", shell=True)
            except Exception as e:
                logger.warning("Failed to free port %d: %s", DEFAULT_JEKYLL_PORT, e)
            if env_id == "ubuntu":
                is_ubuntu = True
            else:
                if env_id:
                    print("Setup only works on Windows and Ubuntu OS (best-effort for other Linux).")
        elif sys.platform == "win32":
            build = windows_build_number()
            if build >= 22000:
                is_windows_supported = True
            else:
                logger.error("Unsupported Windows version. This script supports Windows 11 (build >= 22000) only.")
                return
        else:
            logger.error("Setup only works on Windows and Ubuntu OS (best-effort for other Linux).")
            return

        s = Setup(repo_root=repo_root, ubuntu=is_ubuntu, github_actions=is_github_actions, windows=is_windows_supported)

        full = False
        if len(sys.argv) > 1 and sys.argv[1].lstrip("-").lower() == "full":
            full = True

        if has_internet_connection():
            if full:
                s.full_setup()
            else:
                s.start_server()
        else:
            if full:
                logger.error("A full setup requires an internet connection. You may continue without the full option.")
            else:
                s.start_server()
    except Exception as e:
        logger.exception("Fatal error in setup: %s", e)
        raise


if __name__ == "__main__":
    main()
# This script is intended to be run as a standalone program.