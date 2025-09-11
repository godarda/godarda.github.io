"""
Author: Shubham Darda
Description: Compiles most of the GoDarda website's code snippets from HTML sources.
"""

import os
import re
import sys
import subprocess
from typing import Tuple, Optional
from utilities import config, stats, load_expected_data

# Mapping of extensions to comment styles and compiler commands
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
    match = re.search(r'<pre class="code">(.+?){%- endhighlight -%}</pre>', html, flags=re.DOTALL)
    return match.group(1) if match else None


def get_compiler(extension: str, path: list) -> Tuple[str, str]:
    args = ""
    if extension == ".asm":
        compiler = "nasm -fmacho64" if config.is_macos else "nasm -felf64"
    elif extension == ".cpp":
        compiler = "g++"
        if path[1] == "opengl":
            args = " -framework OpenGL -framework GLUT" if config.is_macos else " -lGL -lGLU -lglut"
        elif path[0] == "cg":
            args = " -lgraph" if config.is_ubuntu else ""
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


def attempt_compilation(source_file: str, html_input: str, compiler: str, subpath: str, file_name: str, extension: str, args: str) -> None:
    try:
        output = extract_code_block(html_input)
        if not output:
            return

        os.makedirs(subpath, exist_ok=True)
        file_path = os.path.join(subpath, file_name + extension)

        header = build_header_block(source_file, file_name, extension)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(header + "\n" + output)

        # Remove first non-header line
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        header_end = next((i for i, line in enumerate(lines) if line.strip() == ""), 0)
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines[:header_end+1] + lines[header_end+2:])

        if config.is_macos or config.is_ubuntu:
            try:
                cmd = f"{compiler} {file_path}{args}"
                subprocess.run(cmd, shell=True, check=True, stderr=subprocess.DEVNULL)
                stats.compiled += 1
            except subprocess.CalledProcessError:
                stats.uncompiled_entries.append(subpath + file_name)
                stats.uncompiled += 1

    except Exception as exc:
        print(exc)


def compile_snippets(source: str, destination: str) -> Optional[Tuple[int, int]]:
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
            subpath = f"{path[0]}/{path[1]}/"
            os.makedirs(subpath, exist_ok=True)

            source_file = os.path.join(source, url + ".html")
            with open(source_file, "r", encoding="utf-8") as f:
                html_input = f.read()

            for lang, ext in {
                    "c": ".c",
                    "cpp": ".cpp",
                    "java": ".java",
                    "nasm": ".asm",
                    "python": ".py",
                    "rust": ".rs",
                    "shell": ".sh"
                }.items():

                if f'<pre class="code">{{%- highlight {lang} -%}}' in html_input:
                    if ext == ".java" and path[0] != "java":
                        continue
                    if ext == ".java" and path[1] == "jdbc":
                        continue
                    if ext == ".cpp" and path[0] == "cg" and path[1] != "opengl":
                        continue
                    compiler, args = get_compiler(ext, path)
                    attempt_compilation(source_file, html_input, compiler, subpath, path[2], ext, args)
                    break
    finally:
        os.chdir(original_cwd)

    return stats.compiled, stats.uncompiled