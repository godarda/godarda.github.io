"""
Author: Shubham Darda
Description: Most of the GoDarda website's programs are compiled by this script.
"""

import os
import re
import shutil
import subprocess
import platform
from typing import Tuple, Optional
from utilities import config, stats, load_expected_data


def is_compiled(html_input: str, compiler: str, subpath: str, file_name: str, extension: str, args: str) -> None:
    """
    Extract code block from provided HTML, write it to a file, remove the first line,
    and attempt to compile using the provided compiler.
    """
    try:
        match = re.search(r'<pre class="code">(.+?){%- endhighlight -%}</pre>', html_input, flags=re.DOTALL)
        if not match:
            return

        output = match.group(1)
        os.makedirs(subpath, exist_ok=True)
        file_path = os.path.join(subpath, file_name + extension)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(output)

        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if len(lines) > 0:
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(lines[1:])

        try:
            cmd = f"{compiler} {file_path}{args}"
            subprocess.run(cmd, shell=True, check=True, stderr=subprocess.DEVNULL)
            stats.compiled += 1
        except subprocess.CalledProcessError:
            stats.uncompiled_entries.append(config.base_url + subpath + file_name)
            stats.uncompiled += 1

    except Exception as exc:
        print(exc)


def compile_codes(source: str, destination: str, data_path: str) -> Optional[Tuple[int, int]]:
    """
    Walk through expected data paths, extract code snippets from HTML pages and try to compile them.
    Returns a tuple (passed, failed) when running on supported platforms.
    """
    if not (config.is_macos or config.is_ubuntu):
        print("Code compilation only supported on macOS or Ubuntu Linux.")
        return None

    os.makedirs(destination, exist_ok=True)
    original_cwd = os.getcwd()
    try:
        os.chdir(destination)
        paths = load_expected_data(config.datapath)

        for entry in paths:
            url = entry.get("url")
            if not url or url.count("/") != 2:
                continue

            path = url.split("/")
            subpath = path[0] + "/" + path[1] + "/"
            os.makedirs(subpath, exist_ok=True)

            args = ""
            source_file = os.path.join(source, url + ".html")
            with open(source_file, "r", encoding="utf-8") as f1:
                html_input = f1.read()

            # Dispatch based on language block
            if '<pre class="code">{%- highlight nasm -%}' in html_input:
                extension = ".asm"
                compiler = "nasm -fmacho64" if config.is_macos else "nasm -felf64"
                is_compiled(html_input, compiler, subpath, path[2], extension, args)

            elif '<pre class="code">{%- highlight c -%}' in html_input:
                extension = ".c"
                compiler = "gcc"
                is_compiled(html_input, compiler, subpath, path[2], extension, args)

            elif '<pre class="code">{%- highlight cpp -%}' in html_input:
                extension = ".cpp"
                compiler = "g++"
                if path[1] == "opengl":
                    args = " -framework OpenGL -framework GLUT" if config.is_macos else " -lGL -lGLU -lglut"
                elif path[0] == "cg":
                    args = " -lgraph" if config.is_ubuntu else ""  # Skip unsupported lib on macOS
                if not (path[0] == "cg" and path[1] != "opengl"):
                    is_compiled(html_input, compiler, subpath, path[2], extension, args)

            elif (
                '<pre class="code">{%- highlight java -%}' in html_input
                and path[0] == "java"
                and path[1] != "jdbc"
            ):
                extension = ".java"
                compiler = "javac"
                is_compiled(html_input, compiler, subpath, path[2], extension, args)

            elif '<pre class="code">{%- highlight shell -%}' in html_input:
                extension = ".sh"
                compiler = "bash -n" if config.is_macos else "shc -f"
                is_compiled(html_input, compiler, subpath, path[2], extension, args)

            elif '<pre class="code">{%- highlight python -%}' in html_input:
                extension = ".py"
                compiler = "python3 -m py_compile"
                is_compiled(html_input, compiler, subpath, path[2], extension, args)

            elif '<pre class="code">{%- highlight rust -%}' in html_input:
                extension = ".rs"
                compiler = "rustc"
                is_compiled(html_input, compiler, subpath, path[2], extension, args)

    finally:
        os.chdir(original_cwd)
        try:
            shutil.rmtree(destination)
        except Exception:
            pass

    return stats.compiled, stats.uncompiled