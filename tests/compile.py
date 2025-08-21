"""
Author: Shubham Darda
Description: Most of the GoDarda website's programs are compiled by this script.
"""

import os
import re
import subprocess
from typing import Tuple, Optional
from utilities import config, stats, load_expected_data


def is_compiled(html_input: str, compiler: str, subpath: str, file_name: str, extension: str, args: str) -> None:
    """
    Extract code block from provided HTML, write it to a file, remove the first line
    (the highlighting directive), and attempt to compile using the provided compiler.

    Parameters:
    - html_input: full HTML content of the page
    - compiler: compiler command (may include flags), e.g. "gcc"
    - subpath: directory relative path where temporary file will be written
    - file_name: base name for the temporary file (no extension)
    - extension: file extension including the dot, e.g. ".c"
    - args: additional arguments appended to the compiler command
    """

    try:
        # Find the inner code block text between the <pre class="code"> and the endhighlight tag.
        # Keep DOTALL so '.' matches newlines.
        match = re.search(r'<pre class="code">(.+?){%- endhighlight -%}</pre>', html_input, flags=re.DOTALL)
        if not match:
            return

        output = match.group(1)

        # Ensure target directory exists (caller usually creates it, but be defensive).
        os.makedirs(subpath, exist_ok=True)
        file_path = os.path.join(subpath, file_name + extension)

        # Write extracted code to file, then remove the first line (highlight directive).
        # Using Python to remove the first line is more portable than invoking sed.
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(output)

        # Read back and drop the first line if the file has more than one line.
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if len(lines) > 0:
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(lines[1:])

        # Attempt to compile using subprocess. Keep behavior similar to the original:
        # redirect stderr to DEVNULL and treat non-zero exit as compilation failure.
        try:
            cmd = f"{compiler} {file_path}{args}"
            subprocess.run(cmd, shell=True, check=True, stderr=subprocess.DEVNULL)
            # Code compiled successfully
            # print("Compiled: " + config.base_url + subpath + file_name)
            stats.compiled += 1
        except subprocess.CalledProcessError:
            # Compilation failed (missing headers/resources or compile errors)
            stats.uncompiled_entries.append(config.base_url + subpath + file_name)
            stats.uncompiled += 1

    except Exception as exc:
        # Report unexpected errors but do not raise to keep behavior consistent.
        print(exc)


def compile_codes(source: str, destination: str, data_path: str) -> Optional[Tuple[int, int]]:
    """
    Walk through expected data paths, extract code snippets from HTML pages and try to compile them.
    Returns a tuple (passed, failed) when running on Ubuntu; otherwise prints a message.

    Parameters:
    - source: path prefix where source HTML files exist
    - destination: temporary working directory used during compilation
    - data_path: path to data (not directly used here; kept for compatibility)
    """
    if not config.is_ubuntu:
        print("Code compilation only works on Ubuntu Linux distribution.")
        return None

    # Create destination and switch into it to mimic original behavior.
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
            subpath = path[0] + "/" + path[1] + "/"  # preserve original subpath format
            os.makedirs(subpath, exist_ok=True)

            args = ""
            source_file = os.path.join(source, url + ".html")
            # Read the HTML content
            with open(source_file, "r", encoding="utf-8") as f1:
                html_input = f1.read()

            # Detect language blocks and dispatch to is_compiled accordingly.
            if '<pre class="code">{%- highlight nasm -%}' in html_input:
                extension = ".asm"
                compiler = "nasm -felf64"
                is_compiled(html_input, compiler, subpath, path[2], extension, args)
            elif '<pre class="code">{%- highlight c -%}' in html_input:
                extension = ".c"
                compiler = "gcc"
                is_compiled(html_input, compiler, subpath, path[2], extension, args)
            elif '<pre class="code">{%- highlight cpp -%}' in html_input:
                if path[1] == "opengl":
                    args = " -lGL -lGLU -lglut"
                elif path[0] == "cg":
                    args = " -lgraph"
                extension = ".cpp"
                compiler = "g++"
                # preserve original conditional behavior for 'cg' non-opengl pages
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
                compiler = "shc -f"
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
        # Restore original working directory and clean up the temporary destination.
        os.chdir(original_cwd)
        # Remove the temporary directory tree created earlier (preserve original behavior).
        try:
            # Use rm -rf to match previous behavior; caller expects the directory removed.
            subprocess.run(["rm", "-rf", destination], check=False)
        except Exception:
            pass

    return stats.compiled, stats.uncompiled
