# Repository Guide

Welcome to GoDarda!  
Whether you're here to contribute, need support, or just exploring how things work, this guide is your starting point.

It’s designed to help you navigate GoDarda’s architecture, workflows, and contributor resources with clarity and confidence.

From onboarding to CI pipelines, from tech stack insights to contributor recognition, every step is crafted to be cross-platform, intentional, and empowering.

## 📚 Table of Contents

- [Introduction](#introduction) 
- [Project Status](#project-status)
- [Cross-Platform CI Status](#cross-platform-ci-status)
- [Technology Stack](#technology-stack)
- [Contribution Guide](CONTRIBUTING.md)
- [Support Guide](SUPPORT.md)
- [Contributors](#contributors)
- [License](#license)

## Introduction

GoDarda is an educational, Jekyll-powered website and companion Android app that provides concise programming examples, tutorials, and curated learning paths across many languages and domains. The repo groups runnable example code under language-specific folders and pairs each example with a documentation page so contributors and learners can quickly find, run, and improve samples.

This repository is intended for:
- learners looking for minimal, runnable examples;
- contributors who add examples, fix documentation, or improve CI/setup scripts;
- maintainers who want a clear, testable site that can be served locally and on GitHub Pages.

Key repo entry points:
- Content & Site Pages: [`pages`](pages/)
- Source Examples (Grouped by Language): [`codes`](codes/)
- Static Assets & ID Maps: [`assets`](assets/)
- Local Setup Scripts: [`setups`](setups/)
- Layouts & Includes: [`_layouts`](_layouts/) & [`_includes`](_includes/)
- CI & Automation: [`.github`](.github/)
- Android App Sources: [`android`](android/)
- Tests & Verification: [`tests`](tests/)

## Project Status

Real-time indicators of GoDarda's health, activity, and platform coverage:

> 🖥️ Platform & Availability

![Platform Support][gdcdhdg] ![GoDarda Android App][gdyzyvk]

> 📦 Repository Metadata

![License][gdycyiw] ![Repo Size][gdypvzk] ![Contributors][gdpgpdw]

> 📈 Activity & Health

![Commits Last Month][gdkgddy] ![Last Commit][gdzveyt] ![Issues][gddaakl] ![Pull Requests][gdwgvye] ![Discussions][gdgnlyl]

## Cross-Platform CI Status
Automated CI workflows are available for macOS, Ubuntu, and Windows. It validates the setup logic and ensure platform-specific compatibility.

| Platform | Status Badge |
|----------|--------------|
| macOS    | [![macOS CI][gdzytwa]][gdzynzx] |
| Ubuntu   | [![Ubuntu CI][gdkvdbh]][gdiagyq] |
| Windows  | [![Windows CI][gdwwzzn]][gdabdte] |

## Technology Stack

GoDarda's website and Android app are version-controlled via GitHub using Git, and built with:

| Category                     | Tools & Technologies                                                                 |
|-----------------------------|----------------------------------------------------------------------------------------|
| Web & Mobile Platforms      | Jekyll, Bootstrap, jQuery, Font Awesome, Google Fonts, HTML5 & CSS3, Liquid, Markdown, Kotlin, Gradle |
| Build, Automation & Diagnostics | Ruby, Bundler, YAML, GitHub Actions, Python, CI Badges                             |
| Engagement & Insights       | Giscus, Google Analytics 4 (GA4)                                                      |
| IDE & Development Environment | Visual Studio Code, GitHub Codespaces, Android Studio                               |

## Contributors

We celebrate every contributor who helps make GoDarda better. Here's a snapshot of the amazing minds behind the project:

![Contributors][gddndwy]

> Want to see your avatar here? Fork the repo, make a meaningful contribution, and submit a pull request!  Not sure where to start? Check out our [Contribution Guide](CONTRIBUTING.md) for everything you need from setup to submission.

## License
This project is licensed under the [GPL-3.0 license][gdaepzd]<br>
© GoDarda, Since 2018.

# Thank You!
GoDarda isn't just code - it's a shared vision. Every contributor, every suggestion, every line of thoughtful markup helps shape a space where clarity meets creativity.

Whether you fixed a typo, refactored a snippet, improved onboarding, or simply explored the repo - thank you. Your presence here means the mission is working.

We believe in recognition without noise, collaboration without ego, and learning without limits. So from the first `git clone` to your latest pull request:  **You're part of something that's built to empower.**

Keep Learning, Keep Building, Keep Inspiring

[gdzwfwc]: https://github.com/godarda/godarda.github.io?tab=MIT-1-ov-file
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
[gdzytwa]: https://github.com/godarda/godarda.github.io/actions/workflows/macos.yml/badge.svg?branch=develop 
[gdzynzx]: https://github.com/godarda/godarda.github.io/actions/workflows/macos.yml  
[gdkvdbh]: https://github.com/godarda/godarda.github.io/actions/workflows/ubuntu.yml/badge.svg?branch=develop  
[gdiagyq]: https://github.com/godarda/godarda.github.io/actions/workflows/ubuntu.yml  
[gdwwzzn]: https://github.com/godarda/godarda.github.io/actions/workflows/windows.yml/badge.svg?branch=develop  
[gdabdte]: https://github.com/godarda/godarda.github.io/actions/workflows/windows.yml
[gddndwy]: https://contrib.rocks/image?repo=godarda/godarda.github.io
[gdaepzd]: https://github.com/godarda/godarda.github.io/blob/main/LICENSE