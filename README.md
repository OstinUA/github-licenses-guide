# 📜 GitHub Licenses Guide: All 13 Default Templates Explained

> 🌐 **Translations:** [English](README.md) | [Українська](README.uk.md) | [Русский](README.ru.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [简体中文](README.zh.md) | [Português](README.pt.md)

When creating a new repository or adding a license on GitHub, you are presented with **13 default license templates**. Choosing the wrong one can either expose you to patent risks, allow corporations to close your code against your wishes, or scare away developers from using your library.

This repository explains what each of the 13 GitHub licenses gives you, how they differ, and which one you should pick.

---

## 📊 Quick Comparison Table

| License | Category | Commercial Use | Can Close Source? | Must Keep Copyright? | Explicit Patent Grant? | Same License Required? |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **CC0 1.0 Universal** | Public Domain | ✅ | ✅ | ❌ No | ❌ Explicitly excluded | ❌ No |
| **The Unlicense** | Public Domain | ✅ | ✅ | ❌ No | ❌ No | ❌ No |
| **MIT License** | Permissive | ✅ | ✅ | ✅ Yes | ❌ No | ❌ No |
| **Boost 1.0 (BSL-1.0)** | Permissive | ✅ | ✅ | ⚠️ Source only | ❌ No | ❌ No |
| **BSD 2-Clause** | Permissive | ✅ | ✅ | ✅ Yes | ❌ No | ❌ No |
| **BSD 3-Clause** | Permissive | ✅ | ✅ | ✅ Yes | ❌ No | ❌ No (+ Non-endorsement) |
| **Apache License 2.0** | Permissive | ✅ | ✅ | ✅ Yes (+ Notices) | ✅ **Yes** | ❌ No |
| **Mozilla Public 2.0** | Weak Copyleft | ✅ | ⚠️ Combined works | ✅ Yes | ✅ **Yes** | ⚠️ Modified files only |
| **Eclipse Public 2.0** | Weak Copyleft | ✅ | ⚠️ Combined works | ✅ Yes | ✅ **Yes** | ⚠️ Modules only |
| **GNU LGPL v2.1** | Weak Copyleft | ✅ | ⚠️ Dynamic linking | ✅ Yes | ❌ Implicit | ⚠️ Library changes only |
| **GNU GPL v2.0** | Strong Copyleft | ✅ | ❌ **No** | ✅ Yes | ⚠️ Implicit | ✅ **Yes (Entire project)** |
| **GNU GPL v3.0** | Strong Copyleft | ✅ | ❌ **No** | ✅ Yes | ✅ **Yes** | ✅ **Yes (+ Anti-Tivoization)** |
| **GNU AGPL v3.0** | Network Copyleft| ✅ | ❌ **No** | ✅ Yes | ✅ **Yes** | ✅ **Yes (+ Cloud/SaaS use)** |

---

## 1. 🕊️ Public Domain (No Rights Reserved)
*Take it, do whatever you want, you don't even have to mention my name.*

### **Creative Commons Zero v1.0 Universal (CC0-1.0)**
* **What it gives:** Waives all copyright and related rights worldwide. Anyone can copy, modify, or sell the work without attribution. Includes a legal fallback license for countries where waiving copyright is not legally possible.
* **Key difference:** Explicitly states that it **does not grant patent rights**. Because of this, it is not recommended for complex software code, as a contributor could theoretically sue users over software patents.
* **Best for:** Datasets, databases, documentation, game assets, media, and small config/code snippets.

### **The Unlicense**
* **What it gives:** A public domain dedication designed specifically for software code. Dedicates code to the public domain with a simple fallback license.
* **Key difference:** Simpler and shorter than CC0, written in developer-friendly language rather than heavy legal prose.
* **Best for:** Small scripts, utilities, and projects where the author wants zero restrictions and zero attribution requirements.

---

## 2. 🤝 Permissive Licenses
*Do whatever you want (even in proprietary commercial products), just keep my copyright notice and don't sue me.*

### **MIT License**
* **What it gives:** The most popular open-source license in the world. Short, simple, allows anyone to reuse code in open or closed projects as long as the original `LICENSE` and copyright notice are included.
* **Key difference:** Extremely brief (less than 200 words), no explicit patent clauses.
* **Best for:** Web frameworks, npm/PyPI packages, indie projects, and libraries aiming for maximum adoption.

### **Apache License 2.0**
* **What it gives:** Full freedom to use, modify, and distribute commercially or privately.
* **Key difference:** Includes strong **Patent Grant** and **Patent Retaliation** clauses (if you sue over patents in the project, you lose your license). Requires documenting notice of changes in modified files and preserving a `NOTICE` file if present.
* **Best for:** Enterprise software, serious libraries, AI models, and corporate open-source projects.

### **BSD 2-Clause "Simplified" License**
* **What it gives:** Almost identical to the MIT license. Allows commercial and private redistribution as long as copyright notices are kept in source and binary distributions.
* **Key difference:** Structured cleanly into two numbered clauses (1. Source distribution, 2. Binary distribution).
* **Best for:** System software, C/C++ libraries, and BSD/Unix ecosystem tools.

### **BSD 3-Clause "New" or "Revised" License**
* **What it gives:** Everything in BSD 2-Clause, plus an extra protection clause for the author's brand.
* **Key difference:** Adds **Clause 3 (Non-endorsement)**: prohibits using the names of the author or contributors to promote or endorse derivative products without written permission.
* **Best for:** Research projects, university code, and corporate tools where brand reputation matters.

### **Boost Software License 1.0 (BSL-1.0)**
* **What it gives:** Ultra-permissive license originally created for C++ libraries.
* **Key difference:** Does **not** require keeping copyright notices when distributing compiled binaries (`.exe`, `.dll`, mobile apps) — attribution is only required when distributing source code.
* **Best for:** Header-only C++/Rust libraries and game development tools where shipping binary legal notices is inconvenient.

---

## 3. 🧩 Weak Copyleft Licenses
*You can use my library inside your closed-source commercial app, as long as any changes you make to MY files remain open-source.*

### **Mozilla Public License 2.0 (MPL-2.0)**
* **What it gives:** File-level copyleft. You can combine MPL-2.0 code with proprietary files in the same project.
* **Key difference:** Copyleft applies strictly per **file**. If you modify an MPL-2.0 file, you must share those modifications under MPL-2.0, but your own new files stay 100% private. Includes explicit patent protection.
* **Best for:** Libraries and core engines where you want community improvements back without scaring off commercial users.

### **Eclipse Public License 2.0 (EPL-2.0)**
* **What it gives:** Business-friendly weak copyleft used widely in the Java and enterprise ecosystem.
* **Key difference:** Allows commercial licensing of combined works and includes modern exceptions for secondary licenses (like GPL-2.0+ compatibility) and explicit patent grants.
* **Best for:** Enterprise plugins, IDEs, and Java frameworks.

### **GNU Lesser General Public License v2.1 (LGPL-2.1)**
* **What it gives:** Library-focused copyleft. Proprietary programs can dynamically link to an LGPL library without becoming open-source.
* **Key difference:** Users of your closed product must be able to replace or relink the LGPL library version. Static linking into closed binaries is tricky and requires providing object files.
* **Best for:** C/C++ shared libraries (`.so`, `.dll`) that want to prevent competitors from making closed forks of the library itself.

---

## 4. 🛡️ Strong & Network Copyleft Licenses
*Freedom is mandatory: if you distribute a project using my code, the ENTIRE project must be open-source under the same license.*

### **GNU General Public License v2.0 (GPL-2.0)**
* **What it gives:** Classic strong copyleft made famous by the Linux Kernel. Any distributed derivative work must provide full source code under GPL-2.0.
* **Key difference:** Does not prohibit hardware lockdown ("Tivoization" — where code is open, but hardware blocks modified versions from running) and lacks the explicit patent clauses of v3.
* **Best for:** Projects working within the Linux kernel ecosystem.

### **GNU General Public License v3.0 (GPL-3.0)**
* **What it gives:** Modernized strong copyleft. Any project using GPL-3.0 code must be open-sourced under GPL-3.0 when distributed.
* **Key difference:** Adds explicit **patent protection**, **Anti-Tivoization** (requires providing installation keys for consumer hardware so users can run modified code), and prevents DRM restrictions.
* **Best for:** Standalone applications, desktop software, and open-source advocates who never want their work turned into proprietary products.

### **GNU Affero General Public License v3.0 (AGPL-3.0)**
* **What it gives:** The strictest open-source license on GitHub. Closes the "Cloud/SaaS Loophole" of GPL-3.0.
* **Key difference:** In standard GPL, if a company runs modified code on their own servers as a web service (SaaS) without distributing the binary, they don't have to share the source. **AGPL-3.0 forces anyone running the modified software over a network (web/cloud) to provide the full source code to users.**
* **Best for:** Self-hosted web apps, databases, and server software that want to prevent cloud giants from monetizing their work without contributing back.

---

## 🎯 TL;DR — How to Choose in 10 Seconds

* **I want zero restrictions (for data/assets):** `Creative Commons Zero v1.0 Universal`
* **I want a simple, popular license for code:** `MIT License`
* **I want a permissive license with strong patent protection:** `Apache License 2.0`
* **I don't want people promoting their forks with my name:** `BSD 3-Clause`
* **I don't want binary apps to carry my copyright notice:** `Boost Software License 1.0`
* **I want improvements to my files shared back, but allow closed apps:** `Mozilla Public License 2.0`
* **I want any app using my code to be 100% open-source:** `GNU GPL v3.0`
* **I want even Cloud/SaaS users of my code to open their changes:** `GNU AGPL v3.0`
