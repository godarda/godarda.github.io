#!/usr/bin/env python3
"""
Code Compilation Test Script (tests/compile.py)

Purpose:
This script extracts and compiles code snippets from generated HTML pages to
ensure that code examples in the documentation are syntactically valid. It
handles parsing, file generation, and toolchain invocation.

Key Features:
1. Extraction: Parses HTML files to locate code blocks.
2. Preparation: Writes code to temporary source files with appropriate headers.
3. Validation: Attempts to compile or syntax-check snippets using installed toolchains.
"""

import os
import re
import sys
import subprocess
from typing import Tuple, Optional
from utilities import CONFIG, STATS, load_expected_data

# Configuration mapping for supported file extensions.
# Defines the comment syntax and the command to retrieve the compiler version.
LANGUAGE_STYLES = {
    '.asm':  {'comment': ';',    'compiler': ['nasm', '-v']},
    '.c':    {'comment': '//',   'compiler': ['gcc', '--version']},
    '.cpp':  {'comment': '//',   'compiler': ['g++', '--version']},
    '.cs':   {'comment': '//',   'compiler': ['dotnet', '--version']},
    '.fs':   {'comment': '//',   'compiler': ['dotnet', '--version']},
    '.java': {'comment': '//',   'compiler': ['java', '-version']},
    '.lisp': {'comment': ';',    'compiler': ['clisp', '--version']},
    '.py':   {'comment': '#',    'compiler': [sys.executable, '--version']},
    '.rs':   {'comment': '//',   'compiler': ['rustc', '--version']},
    '.sh':   {'comment': '#',    'compiler': ['bash', '--version']},
}


def extract_code_block(html: str) -> Optional[str]:
    """
    Extracts the raw code block text from the provided HTML content.

    Args:
        html: The HTML content string.

    Returns:
        The extracted code string if found, otherwise None.
    """
    match = re.search(r'<pre class="code">(.+?){%- endhighlight -%}</pre>', html, flags=re.DOTALL)
    return match.group(1) if match else None


def get_compiler(extension: str, path: list) -> Tuple[str, str]:
    """
    Determines the appropriate compiler command and arguments for a given file extension.

    Args:
        extension: The file extension (e.g., '.cpp').
        path: The URL path segments, used for applying specific compilation flags.

    Returns:
        A tuple containing the compiler command and any additional arguments.
    """
    args = ""
    if extension == ".asm":
        compiler = "nasm -fmacho64" if CONFIG.OS_NAME == "macOS" else "nasm -felf64"
    elif extension == ".cpp":
        compiler = "g++"
        if path[1] == "opengl":
            args = " -framework OpenGL -framework GLUT" if CONFIG.OS_NAME == "macOS" else " -lGL -lGLU -lglut"
        elif path[0] == "cg":
            args = " -lgraph" if CONFIG.OS_NAME == "Ubuntu" else ""
    elif extension == ".java":
        compiler = "javac"
    elif extension == ".sh":
        compiler = "bash -n"
    elif extension == ".py":
        compiler = "python3 -m py_compile"
    elif extension == ".rs":
        compiler = "rustc"
    elif extension == ".c":
        compiler = "gcc"
    else:
        compiler = ""
    return compiler, args


def build_header_block(file_path: str, file_name: str, extension: str) -> str:
    """
    Generates a comment header for the source file.

    Args:
        file_path: Path to the original HTML file (used to extract the title).
        file_name: The base name of the file.
        extension: The file extension.

    Returns:
        A formatted string containing metadata about the file and toolchain.
    """
    style = LANGUAGE_STYLES.get(extension)
    cmd = style.get('compiler', []) if style else []
    result = subprocess.check_output(cmd, stderr=subprocess.STDOUT)

    title = ""
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip().startswith('title:'):
                title = line.strip().split(':', 1)[1].strip()
                break

    comment = style['comment'] if style else None
    compiler_hint = next((line for line in result.decode().splitlines() if line.strip()), '')

    header_fields = {
        'Title': title,
        'File Name': os.path.basename(file_name + extension),
        'Compiled': compiler_hint,
        'Author': 'GoDarda',
        'License': 'GNU General Public License',
    }

    lines = [f"{comment} " + "-" * 100]
    lines += [f"{comment} {key:<15}: {value}" for key, value in header_fields.items()]
    lines.append(f"{comment} " + "-" * 100 + "\n")
    return '\n'.join(lines)


def attempt_compilation(source_file: str, html_content: str, compiler: str, output_dir: str, file_name: str, extension: str, args: str) -> None:
    """
    Extracts code, writes it to disk, and attempts compilation.

    Updates the global stats object with the result (compiled/uncompiled).
    Exceptions are caught and logged to allow the process to continue.
    """
    try:
        output = extract_code_block(html_content)
        if not output:
            return

        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, file_name + extension)

        header = build_header_block(source_file, file_name, extension)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(header + "\n" + output)

        # Remove the first line after the header to clean up potential formatting artifacts.
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        header_end = next((i for i, line in enumerate(lines) if line.strip() == ""), 0)
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines[:header_end+1] + lines[header_end+2:])

        if CONFIG.OS_NAME in ("macOS", "Ubuntu"):
            try:
                cmd = f"{compiler} {file_path}{args}"
                subprocess.run(cmd, shell=True, check=True, stderr=subprocess.DEVNULL)
                STATS.compiled += 1
            except subprocess.CalledProcessError:
                STATS.uncompiled_entries.append(output_dir + file_name)
                STATS.uncompiled += 1

    except Exception as exc:
        print(f"Failed to process {file_name}{extension}: {exc}")


def compile_snippets(source: str, destination: str) -> Optional[Tuple[int, int]]:
    """
    Scans the source directory for HTML files and attempts to compile extracted code snippets.

    Returns:
        A tuple of (compiled_count, uncompiled_count) if the OS is supported,
        otherwise None.
    """
    if CONFIG.OS_NAME not in ("macOS", "Ubuntu"):
        print("Code compilation only supported on macOS or Ubuntu Linux.")
        return None

    # Use absolute path for destination
    destination_path = os.path.abspath(destination)
    os.makedirs(destination_path, exist_ok=True)

    paths = load_expected_data(CONFIG.DATAPATH)
    original_cwd = os.getcwd()

    try:
        os.chdir(destination_path)
        for entry in paths:
            url = entry.get("url")
            if not url or url.count("/") != 2:
                continue

            path = url.split("/")
            # Create absolute output directory path
            output_dir = os.path.join(destination_path, path[0], path[1])
            os.makedirs(output_dir, exist_ok=True)

            source_file = None
            # Locate the corresponding HTML file in the source directory structure.
            for folder in os.listdir(source):
                sub_source_dir = os.path.join(source, folder)
                if os.path.isdir(sub_source_dir):
                    potential_path = os.path.join(sub_source_dir, url + ".html")
                    if os.path.exists(potential_path):
                        source_file = potential_path
                        break
            if not source_file:
                continue
            with open(source_file, "r", encoding="utf-8") as f:
                html_content = f.read()

            for lang, ext in {
                    "c": ".c",
                    "cpp": ".cpp",
                    "java": ".java",
                    "nasm": ".asm",
                    "python": ".py",
                    "rust": ".rs",
                    "shell": ".sh"
                }.items():

                if f'<pre class="code">{{%- highlight {lang} -%}}' in html_content:
                    if ext == ".java" and path[0] != "java":
                        continue
                    if ext == ".java" and path[1] == "jdbc":
                        continue
                    if ext == ".cpp" and path[0] == "cg" and path[1] != "opengl":
                        continue
                    compiler, args = get_compiler(ext, path)
                    attempt_compilation(source_file, html_content, compiler, output_dir, path[2], ext, args)
                    break
    finally:
        os.chdir(original_cwd)

    return STATS.compiled, STATS.uncompiled
