# GoDarda 

A robust, cross-platform static site powered by Jekyll, Bootstrap, and jQuery. Maintained since 2018.

## 📚 Table of Contents

- [Project Status](#project-status)
- [Cross-Platform CI Status](#cross-platform-ci-status)
- [Setup Instructions](#setup-instructions)
  - macOS
  - Ubuntu
  - Windows
- [Technology Stack](#technology-stack)
- [Additional Notes](#additional-notes)
- [License](#license)
- [Contributors](#contributors)

## Project Status

Real-time indicators of GoDarda’s health, activity, and platform coverage:

#### 🖥️ Platform & Availability

![Platform Support](https://img.shields.io/badge/platforms-macOS%2C%20Ubuntu%2C%20Windows-blueviolet?logo=microsoft)
![GoDarda Android App](https://img.shields.io/badge/GoDarda-Android%20App-bluegreen?logo=android)

#### 📦 Repository Metadata

![License](https://img.shields.io/github/license/godarda/godarda.github.io?color=blue&logo=open-source-initiative)
![Repo Size](https://img.shields.io/github/repo-size/godarda/godarda.github.io?color=orange&logo=github)
![Contributors](https://img.shields.io/github/contributors/godarda/godarda.github.io?color=brightgreen&logo=git)

#### 📈 Activity & Health

![Commits Last Month](https://img.shields.io/github/commit-activity/m/godarda/godarda.github.io?color=yellow&logo=git)
![Last Commit](https://img.shields.io/github/last-commit/godarda/godarda.github.io?color=red&logo=github)
![Issues](https://img.shields.io/github/issues/godarda/godarda.github.io?color=purple&logo=github)
![Pull Requests](https://img.shields.io/github/issues-pr/godarda/godarda.github.io?color=cyan&logo=github)
![Discussions](https://img.shields.io/github/discussions/godarda/godarda.github.io?color=gold&logo=github)


## Cross-Platform CI Status
Automated CI workflows are available for macOS, Ubuntu, and Windows:

| Platform | Status Badge |
|----------|--------------|
| macOS    | [![macOS CI](https://github.com/godarda/godarda.github.io/actions/workflows/macos.yml/badge.svg?branch=main)](https://github.com/godarda/godarda.github.io/actions/workflows/macos.yml) |
| Ubuntu   | [![Ubuntu CI](https://github.com/godarda/godarda.github.io/actions/workflows/ubuntu.yml/badge.svg?branch=main)](https://github.com/godarda/godarda.github.io/actions/workflows/ubuntu.yml) |
| Windows  | [![Windows CI](https://github.com/godarda/godarda.github.io/actions/workflows/windows.yml/badge.svg?branch=main)](https://github.com/godarda/godarda.github.io/actions/workflows/windows.yml) |

## Setup Instructions
**Prerequisite for all platforms:** [Git](https://git-scm.com) must be installed and available in your system path.

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
#### **[Windows:](#windows)** Ensure [Visual Studio Code][gdkcqso], [Python][gdxadth], and [Ruby][gdzrvdq] are installed and then follow these steps:
```
PS D:\> Open Visual Studio Code -> Terminal  
PS D:\godarda.github.io> python setups/windows.py full  
```

## Technology Stack

GoDarda's website is version-controlled via [GitHub](https://github.com) using [Git](https://git-scm.com), and built with:

### 🖥️ Frontend
- [Jekyll](https://jekyllrb.com) — Static site generator  
- [Bootstrap](https://getbootstrap.com) — Responsive UI framework  
- [jQuery](https://jquery.com) — DOM manipulation and scripting  
- [Font Awesome](https://fontawesome.com) — Icon toolkit for UI clarity  
- [Google Fonts](https://fonts.google.com) — Typography customization  
- [HTML5 & CSS3](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) — Semantic structure and styling  
- [Liquid](https://shopify.github.io/liquid/) — Templating engine used by Jekyll for dynamic content  
- [Markdown](https://www.markdownguide.org) — Lightweight markup for documentation and contributor guides  

### ⚙️ Build System & Dependencies
- [Ruby](https://www.ruby-lang.org) — Core language powering Jekyll and its plugin ecosystem  
- [Bundler](https://bundler.io) — Dependency manager for Ruby gems used in site generation  
- [YAML](https://yaml.org) — Declarative configuration for workflows, metadata, and site settings  

### 🚀 Automation & CI
- [GitHub Actions](https://github.com/features/actions) — CI/CD workflows for cross-platform validation and automated deployment  
- [CI Badges](https://shields.io) — Status indicators for build health and contributor clarity  
- [Shell scripting (Bash, PowerShell)] — Platform-aware setup and automation logic  

### 🐍 Diagnostics & Reporting
- [Python](https://www.python.org) — Used for resource versioning, diagnostics, and reporting  
  - `requests`, `BeautifulSoup` — Web scraping and test reporting utilities  
- [JSON](https://www.json.org) — Structured data for resource versioning and diagnostics

This stack reflects GoDarda’s commitment to clarity, automation, and contributor empowerment. Every tool is chosen to support maintainability, cross-platform resilience, and a welcoming onboarding experience.

## Additional Notes

- All setup scripts are located in the [`setups/`][gdzgwel] directory and are platform-specific (`macos.py`, `ubuntu.py`, `windows.py`).
- CI workflows validate setup logic and ensure platform-specific compatibility.
- The site runs locally on port `4000` by default. You can access it via `http://127.0.0.1:4000` or `http://localhost:4000`.
- To contribute:
  - Fork this repository to your GitHub account.
  - Create a new branch for your changes.
  - Make your updates and ensure they pass all CI checks.
  - Submit a pull request with a clear description of the changes and rationale.
- If you encounter permission issues or missing dependencies, check your platform-specific prerequisites and ensure Python and Ruby are correctly installed and accessible.

## License
This project is licensed under the [GPL-3.0 license](https://github.com/godarda/godarda.github.io/blob/main/LICENSE)  
© GoDarda, Since 2018.

## Contributors

We celebrate every contributor who helps make GoDarda better. Here's a snapshot of the amazing minds behind the project:

![Contributors](https://contrib.rocks/image?repo=godarda/godarda.github.io)

> Want to see your avatar here? Fork the repo, make a meaningful contribution, and submit a pull request!

[gdezvdy]: https://github.com
[gdzuddz]: https://getbootstrap.com
[gdddcia]: https://jquery.com
[gdwwvga]: https://jekyllrb.com
[gdzyzav]: https://git-scm.com
[gdxadth]: https://www.python.org
[gdzrvdq]: https://rubyinstaller.org/downloads
[gdkcqso]: https://code.visualstudio.com
[gdzdngz]: https://github.com/godarda/godarda.github.io?tab=MIT-1-ov-file
[gdzgwel]: https://github.com/godarda/godarda.github.io/tree/main/setups