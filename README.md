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
- [Contributors](#contributors)
- [Contributor Recognition](#contributor-recognition)
- [Why Recognition Matters](#why-recognition-matters)
- [Support Guide](SUPPORT.md)
- [License](#license)

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
Automated CI workflows are available for macOS, Ubuntu, and Windows. It validates the setup logic and ensure platform-specific compatibility.

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
- All setup scripts are located in the [`setups/`][gdzgwel] directory and are platform-specific (`macos.py`, `ubuntu.py`, `windows.py`).
- The site runs locally on port `4000` by default. You can access it via `http://127.0.0.1:4000` or `http://localhost:4000`.

## Technology Stack

GoDarda's website and Android app are version-controlled via [GitHub](https://github.com) using [Git](https://git-scm.com), and built with:

| Category | Tools & Technologies |
|----------|----------------------|
| 🖥️ Web & Mobile Platforms | [Jekyll](https://jekyllrb.com), [Bootstrap](https://getbootstrap.com), [jQuery](https://jquery.com), [Font Awesome](https://fontawesome.com), [Google Fonts](https://fonts.google.com), [HTML5 & CSS3](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5), [Liquid](https://shopify.github.io/liquid/), [Markdown](https://www.markdownguide.org), [Kotlin](https://kotlinlang.org), [Gradle](https://gradle.org) |
| ⚙️ Build, Automation & Diagnostics | [Ruby](https://www.ruby-lang.org), [Bundler](https://bundler.io), [YAML](https://yaml.org), [GitHub Actions](https://github.com/features/actions), [Python](https://www.python.org), `requests`, `BeautifulSoup`, [CI Badges](https://shields.io) |
| 🌐 Engagement & Insights | [Giscus](https://giscus.app), [Google Analytics 4 (GA4)](https://analytics.google.com) |
| 🧰 IDE & Development Environment | [Visual Studio Code](https://code.visualstudio.com), [GitHub Codespaces](https://github.com/features/codespaces), [Android Studio](https://developer.android.com/studio) |

This stack reflects GoDarda’s commitment to clarity, automation, and contributor empowerment. Every tool is chosen to support maintainability, cross-platform resilience, and a welcoming onboarding experience.

## Contributors

We celebrate every contributor who helps make GoDarda better. Here's a snapshot of the amazing minds behind the project:

![Contributors](https://contrib.rocks/image?repo=godarda/godarda.github.io)

> Want to see your avatar here? Fork the repo, make a meaningful contribution, and submit a pull request!

## Contributor Recognition

At **GoDarda**, we believe every thoughtful contribution deserves to be seen and celebrated. Whether you've refactored code, improved documentation, designed UI elements, or supported others in Discussions — your impact matters.

We offer visual badges to recognize contributors across key areas:

| Badge | Description |
|-------|-------------|
| 🛠️ **Code Contributor** | For meaningful code contributions, refactors, or feature implementations |
| 📖 **Documentation Contributor** | For improving clarity, onboarding, or contributor guides |
| 🎨 **Design Contributor** | For UI/UX enhancements, badge layouts, or visual polish |
| 💡 **Idea Contributor** | For proposing impactful features or architectural improvements |
| 🌱 **Community Builder** | For supporting others, improving contributor experience, or fostering inclusivity |
| 🧪 **Bug Hunter** | For identifying and reporting reproducible issues |
| 🧭 **Maintainer’s Choice** | Special recognition for contributions that go above and beyond |

To request a badge, [submit a badge request here](https://github.com/godarda/godarda.github.io/issues/new?template=badge.yml).

## Why Recognition Matters

Badges aren’t just visual flair — they reflect the spirit of open-source collaboration. They help contributors:
- Build a visible portfolio of impact  
- Feel valued and empowered  
- Inspire others to contribute meaningfully

We review badge requests with care and gratitude. Every contribution helps GoDarda grow into a more inclusive, scalable, and inspiring space.

## License
This project is licensed under the [GPL-3.0 license](https://github.com/godarda/godarda.github.io/blob/main/LICENSE)  
© GoDarda, Since 2018.

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