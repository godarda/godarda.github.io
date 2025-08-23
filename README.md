# GoDarda

A robust, cross-platform static site powered by Jekyll, Bootstrap, and jQuery. Maintained since 2018.


## 📚 Table of Contents

- [License](#license)
- [Design Frameworks](#design-frameworks)
- [Development & Testing](#development--testing)
- [Setup Instructions](#setup-instructions)
  - [macOS](#macos)
  - [Ubuntu](#ubuntu)
  - [Windows](#windows)
- [Additional Notes](#additional-notes)


## 📝 License

This project is licensed under the [MIT License](https://github.com/godarda/godarda.github.io?tab=MIT-1-ov-file)  
© GoDarda, Since 2018.

---

## 🧱 Design Frameworks

GoDarda's website is version-controlled via [GitHub](https://github.com) using [Git](https://git-scm.com), and built with:

- [Jekyll](https://jekyllrb.com) — Static site generator  
- [Bootstrap](https://getbootstrap.com) — Responsive UI framework  
- [jQuery](https://jquery.com) — DOM manipulation and scripting

## ⚙️ Development & Testing

Automated CI workflows are available for macOS, Ubuntu, and Windows:

| Platform | Status Badge |
|----------|--------------|
| macOS    | [![macOS CI](https://github.com/godarda/godarda.github.io/actions/workflows/macos.yml/badge.svg?branch=main)](https://github.com/godarda/godarda.github.io/actions/workflows/macos.yml) |
| Ubuntu   | [![Ubuntu CI](https://github.com/godarda/godarda.github.io/actions/workflows/ubuntu.yml/badge.svg?branch=main)](https://github.com/godarda/godarda.github.io/actions/workflows/ubuntu.yml) |
| Windows  | [![Windows CI](https://github.com/godarda/godarda.github.io/actions/workflows/windows.yml/badge.svg?branch=main)](https://github.com/godarda/godarda.github.io/actions/workflows/windows.yml) |

---

## 🚀 Setup Instructions

**Prerequisite for all platforms:**  
[Git](https://git-scm.com) must be installed and available in your system path.

**Common setup steps:**
```bash
# Clone the repository
git clone https://github.com/godarda/godarda.github.io.git

# Navigate into the project directory
cd godarda.github.io
```

#### **macOS:** Run the following commands to get started:
```
$ python3 setups/macos.py full
```
#### **Ubuntu:** Run the following commands to get started:
```
$ python3 setups/ubuntu.py full
```
#### **Windows:** Ensure [Visual Studio Code][gidkcqso], [Python][gidxadth], and [Ruby][gidzrvdq] are installed. Then clone the repository and follow these steps:
```
PS D:\> Open Visual Studio Code -> Terminal  
PS D:\godarda.github.io> python setups/windows.py full  
```

## 📦 Additional Notes

- All setup scripts are located in the [`setups/`][gidzgwel] directory and are platform-specific (`macos.py`, `ubuntu.py`, `windows.py`).
- CI workflows validate setup logic and ensure platform-specific compatibility.
- The site runs locally on port `4000` by default. You can access it via `http://127.0.0.1:4000` or `http://localhost:4000`.
- To contribute:
  - Fork this repository to your GitHub account.
  - Create a new branch for your changes.
  - Make your updates and ensure they pass all CI checks.
  - Submit a pull request with a clear description of the changes and rationale.
- If you encounter permission issues or missing dependencies, check your platform-specific prerequisites and ensure Python and Ruby are correctly installed and accessible.

[gidezvdy]: https://github.com
[gidzuddz]: https://getbootstrap.com
[gidddcia]: https://jquery.com
[gidwwvga]: https://jekyllrb.com
[gidzyzav]: https://git-scm.com
[gidxadth]: https://www.python.org
[gidzrvdq]: https://rubyinstaller.org/downloads
[gidkcqso]: https://code.visualstudio.com
[gidzdngz]: https://github.com/godarda/godarda.github.io?tab=MIT-1-ov-file
[gidzgwel]: https://github.com/godarda/godarda.github.io/tree/main/setups