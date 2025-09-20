# Contribution Guide

Welcome to the GoDarda contributor community!  
Whether you're here to fix a typo, automate a workflow, or design something entirely new-your contributions matter.  
This space is built to support you with clarity, consistency, and warmth at every step.

We celebrate thoughtful contributions, empower first-time contributors, and believe every improvement shapes the future of open-source learning.

## 📚 Table of Contents

- [Introduction](#introduction)
- [Ways to Contribute](#ways-to-contribute)
- [Original Work Policy](#original-work-policy)
- [Standards & Conventions](#standards--conventions)
- [Pull Request Guidelines](#pull-request-workflow)
- [Getting Started](#getting-started)
- [Contributor Recognition](#contributor-recognition)

## Introduction

This guide explains how to contribute to GoDarda in a consistent, professional, and efficient way.  

It covers common contribution types-documentation, runnable examples, scripts, and bug reports-along with required conventions, the original-work policy, and the pull request workflow.

By following these standards, your contributions will be easier to review, faster to merge, and aligned with GoDarda's long-term goals.  

Every improvement strengthens the clarity, culture, and contributor experience of the project.

## Ways to Contribute

- Improve documentation and examples.
- Add minimal, runnable code samples grouped by language.
- Enhance CI, automation, or setup scripts.
- Report bugs, request features, or help others.

## Standards & Conventions

- Keep examples small, focused, and correct.
- Prefer spaces over tabs and consistent Markdown formatting.
- Use descriptive file names and reserve GDIDs from `assets/gdid_sets/` when adding new examples.
- Include clear front-matter for Jekyll pages (title, permalink, tags).
- Test examples locally before submitting.

## Original Work Policy

All contributions to GoDarda must be **original and authored by you**.

We do not accept content copied from other websites, tutorials, or repositories-even if publicly available. Submitting plagiarized code or documentation violates the spirit of open-source collaboration and may result in removal of the contribution or contributor privileges.

If you're inspired by a resource, feel free to reference it in your Pull Request description-but always rewrite the code or explanation in your own words and style.

> GoDarda is a space for learning, sharing, and growing together. Let's keep it authentic.

## Pull Request Workflow

1. Fork, clone, and checkout `develop`.
2. Create a feature branch: git checkout -b feature/your-change
3. Run platform setup and validate locally.
4. Commit with clear messages and push.
5. Open a PR targeting `develop` with a descriptive title and summary.

Maintainers will review your pull request with these principles in mind. Thoughtful, well-documented contributions make the review process smoother and help uphold the quality of the GoDarda ecosystem.

## Getting Started

We're thrilled to have you contribute! This guide walks you through the full onboarding process from forking the repo to running your local setup and submitting your first contribution. Every step is designed to be clean, empowering, and platform-friendly.

> **Prerequisite for all platforms:** [Git][gdkbvgy] must be installed and available in your system path.

1. **Fork the repository**: [godarda.github.io][gdzenad]  
2. **Clone your fork**:
   ```bash
   $ git clone https://github.com/<your-username>/godarda.github.io
   $ cd godarda.github.io
   ```
3. Switch to the develop branch (this is where all contributions should begin):

   ```bash
   git checkout develop
   ```
4. Create a new branch of develop:
   ```bash
   git checkout -b feature/my-contribution
   ```
5. Run the platform-specific setup script to initialize your environment:
   #### **macOS:**
   ```
   $ python3 setups/macos.py full
   ```
   #### **Ubuntu:**
   ```
   $ python3 setups/ubuntu.py full
   ```
   #### **Windows:** Ensure [Visual Studio Code][gdwyygg], [Python][gdkweoz], and [Ruby][gdkwzyw] are installed and then follow these steps:
   ```
   PS D:\> Open Visual Studio Code -> Terminal  
   PS D:\godarda.github.io> python setups/windows.py full  
   ```
   - All setup scripts are located in the [`setups/`][gdgggza] directory and are platform-specific (`macos.py`, `ubuntu.py`, `windows.py`).
   - The site runs locally on port `4000` by default. You can access it via `http://127.0.0.1:4000` or `http://localhost:4000`.
6. Make your changes  
7. Commit and push:

   ```bash
   git commit -m "Add: new Python example for loops"
   git push origin feature/my-contribution
   ```
8. Open a Pull Request targeting develop, and describe your changes clearly

Important: Please do not open pull requests directly to main. 
The main branch is protected and reserved for monthly squash merges by admins to maintain a clean, readable history.
All contributions should flow through develop, where they'll be reviewed, refined, and eventually merged into main during the monthly sync.

Once submitted, your contribution will go through a review process.  
Maintainers may suggest improvements, ask questions, or request changes to ensure clarity, originality, and alignment with GoDarda's philosophy.  
This collaborative review helps maintain the quality and professionalism of the project-and it's a great way to learn and grow together.

## Contributor Recognition

At **GoDarda**, we believe every thoughtful contribution deserves to be seen and celebrated. Whether you've refactored code, improved documentation, designed UI elements, or supported others in Discussions - your impact matters. Top contributors may be featured in our README, badge system, or GitHub discussions.

We offer visual badges to recognize contributors across key areas:

| Badge | Description |
|-------|-------------|
| **Code Contributor** | For meaningful code contributions, refactors, or feature implementations |
| **Documentation Contributor** | For improving clarity, onboarding, or contributor guides |
| **Design Contributor** | For UI/UX enhancements, badge layouts, or visual polish |
| **Idea Contributor** | For proposing impactful features or architectural improvements |
| **Community Builder** | For supporting others, improving contributor experience, or fostering inclusivity |
| **Bug Hunter** | For identifying and reporting reproducible issues |
| **Maintainer's Choice** | Special recognition for contributions that go above and beyond |

To request a badge, [submit a badge request here][gdxeeiw].

# Thank You!
Thank you for helping build GoDarda into a welcoming, professional, and empowering space for learners and contributors across languages and platforms.  

Your contributions shape not just the code-but the culture, clarity, and spirit of the project.

If you have questions, suggestions, or ideas to improve GoDarda:

- Open an [Issue][gdzbzfc] to report bugs or request features  
- Start a [Discussion][gdzenad] to share thoughts, ask questions, or connect with the community

We're excited to collaborate with you and grow together.

[gdkbvgy]: https://git-scm.com
[gdkweoz]: https://www.python.org
[gdkwzyw]: https://rubyinstaller.org/downloads
[gdwyygg]: https://code.visualstudio.com
[gdzenad]: https://github.com/godarda/godarda.github.io
[gdgggza]: https://github.com/godarda/godarda.github.io/tree/main/setups
[gdzbzfc]: https://github.com/godarda/godarda.github.io/issues
[gdzenad]: https://github.com/godarda/godarda.github.io/discussions
[gdxeeiw]: https://github.com/godarda/godarda.github.io/issues/new?template=badge.yml