# GoDarda Guide

A robust, cross-platform static site powered by [Jekyll][gdarema], [Bootstrap][gdzhvyv], and [jQuery][gdhzgdv]. Maintained since 2018.

## 📚 Table of Contents

- [Project Status](#project-status)
- [Cross-Platform CI Status](#cross-platform-ci-status)
- [Setup Instructions](#setup-instructions)
  - macOS
  - Ubuntu
  - Windows
- [Technology Stack](#technology-stack)
- [Contributors](#contributors)
- [Contribution Guide](CONTRIBUTING.md)
- [Support Guide](SUPPORT.md)
- [License](#license)
- [Thank You](#thank-you)

## Project Status

Real-time indicators of GoDarda’s health, activity, and platform coverage:

#### 🖥️ Platform & Availability

![Platform Support][gdcdhdg]  
![GoDarda Android App][gdyzyvk]

#### 📦 Repository Metadata

![License][gdycyiw]  
![Repo Size][gdypvzk]  
![Contributors][gdpgpdw]

#### 📈 Activity & Health

![Commits Last Month][gdkgddy]  
![Last Commit][gdzveyt]  
![Issues][gddaakl]  
![Pull Requests][gdwgvye]  
![Discussions][gdgnlyl]

## Cross-Platform CI Status
Automated CI workflows are available for macOS, Ubuntu, and Windows. It validates the setup logic and ensure platform-specific compatibility.

| Platform | Status Badge |
|----------|--------------|
| macOS    | [![macOS CI][gdzytwa]][gdzynzx] |
| Ubuntu   | [![Ubuntu CI][gdkvdbh]][gdiagyq] |
| Windows  | [![Windows CI][gdwwzzn]][gdabdte] |

## Setup Instructions
**Prerequisite for all platforms:** [Git][gdkbvgy] must be installed and available in your system path.

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
- All setup scripts are located in the [`setups/`][gdzgwel] directory and are platform-specific (`macos.py`, `ubuntu.py`, `windows.py`).
- The site runs locally on port `4000` by default. You can access it via `http://127.0.0.1:4000` or `http://localhost:4000`.

## Technology Stack

GoDarda's website and Android app are version-controlled via [GitHub][gdzgezt] using [Git][gdkbvgy], and built with:

| Category | Tools & Technologies |
|----------|----------------------|
| 🖥️ Web & Mobile Platforms | [Jekyll][gdarema], [Bootstrap][gdzhvyv], [jQuery][gdhzgdv], [Font Awesome][gdabvvg], [Google Fonts][gdexzgv], [HTML5 & CSS3][gddbwdz], [Liquid][gddiwhy], [Markdown][gdysbav], [Kotlin][gdqoawz], [Gradle][gdgguvy] |
| ⚙️ Build, Automation & Diagnostics | [Ruby][gdzezdk], [Bundler][gdezesc], [YAML][gdvzuav], [GitHub Actions][gdzagzz], [Python][gdkweoz], `requests`, `BeautifulSoup`, [CI Badges][gdwezyg] |
| 🌐 Engagement & Insights | [Giscus][gdksnhv], [Google Analytics 4 (GA4)][gdkzvva] |
| 🧰 IDE & Development Environment | [Visual Studio Code][gdwyygg], [GitHub Codespaces][gdwiezg], [Android Studio][gdpvhmu] |

This stack reflects GoDarda’s commitment to clarity, automation, and contributor empowerment. Every tool is chosen to support maintainability, cross-platform resilience, and a welcoming onboarding experience.

## Contributors

We celebrate every contributor who helps make GoDarda better. Here's a snapshot of the amazing minds behind the project:

![Contributors][gddndwy]

> Want to see your avatar here? Fork the repo, make a meaningful contribution, and submit a pull request!

## License
This project is licensed under the [GPL-3.0 license][gdaepzd]
© GoDarda, Since 2018.

## Thank You!
GoDarda isn’t just code - it’s a shared vision. Every contributor, every suggestion, every line of thoughtful markup helps shape a space where clarity meets creativity.

Whether you fixed a typo, refactored a snippet, improved onboarding, or simply explored the repo - thank you. Your presence here means the mission is working.

We believe in recognition without noise, collaboration without ego, and learning without limits. So from the first `git clone` to your latest pull request:  **You’re part of something that’s built to empower.**

Keep Learning, Keep Building, Keep Inspiring

[gdzgezt]: https://github.com
[gdzhvyv]: https://getbootstrap.com
[gdhzgdv]: https://jquery.com
[gdarema]: https://jekyllrb.com
[gdkbvgy]: https://git-scm.com
[gdkweoz]: https://www.python.org
[gdkwzyw]: https://rubyinstaller.org/downloads
[gdwyygg]: https://code.visualstudio.com
[gdzwfwc]: https://github.com/godarda/godarda.github.io?tab=MIT-1-ov-file
[gdgggza]: https://github.com/godarda/godarda.github.io/tree/main/setups
[gdabvvg]: https://fontawesome.com
[gdexzgv]: https://fonts.google.com
[gddbwdz]: https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5
[gddiwhy]: https://shopify.github.io/liquid
[gdysbav]: https://www.markdownguide.org
[gdqoawz]: https://kotlinlang.org
[gdgguvy]: https://gradle.org
[gdzezdk]: https://www.ruby-lang.org
[gdezesc]: https://bundler.io
[gdvzuav]: https://yaml.org
[gdzagzz]: https://github.com/features/actions
[gdwezyg]: https://shields.io
[gdksnhv]: https://giscus.app
[gdkzvva]: https://analytics.google.com
[gdwiezg]: https://github.com/features/codespaces
[gdpvhmu]: https://developer.android.com/studio
[gdcdhdg]: https://img.shields.io/badge/platforms-macOS%2C%20Ubuntu%2C%20Windows-blueviolet?logo=microsoft  
[gdyzyvk]: https://img.shields.io/badge/GoDarda-Android%20App-bluegreen?logo=android  
[gdycyiw]: https://img.shields.io/github/license/godarda/godarda.github.io?color=blue&logo=open-source-initiative  
[gdypvzk]: https://img.shields.io/github/repo-size/godarda/godarda.github.io?color=orange&logo=github  
[gdpgpdw]: https://img.shields.io/github/contributors/godarda/godarda.github.io?color=brightgreen&logo=git  
[gdkgddy]: https://img.shields.io/github/commit-activity/m/godarda/godarda.github.io?color=yellow&logo=git  
[gdzveyt]: https://img.shields.io/github/last-commit/godarda/godarda.github.io?color=red&logo=github  
[gddaakl]: https://img.shields.io/github/issues/godarda/godarda.github.io?color=purple&logo=github  
[gdwgvye]: https://img.shields.io/github/issues-pr/godarda/godarda.github.io?color=cyan&logo=github  
[gdgnlyl]: https://img.shields.io/github/discussions/godarda/godarda.github.io?color=gold&logo=github
[gdzytwa]: https://github.com/godarda/godarda.github.io/actions/workflows/macos.yml/badge.svg?branch=main  
[gdzynzx]: https://github.com/godarda/godarda.github.io/actions/workflows/macos.yml  
[gdkvdbh]: https://github.com/godarda/godarda.github.io/actions/workflows/ubuntu.yml/badge.svg?branch=main  
[gdiagyq]: https://github.com/godarda/godarda.github.io/actions/workflows/ubuntu.yml  
[gdwwzzn]: https://github.com/godarda/godarda.github.io/actions/workflows/windows.yml/badge.svg?branch=main  
[gdabdte]: https://github.com/godarda/godarda.github.io/actions/workflows/windows.yml
[gddndwy]: https://contrib.rocks/image?repo=godarda/godarda.github.io
[gdaepzd]: https://github.com/godarda/godarda.github.io/blob/main/LICENSE