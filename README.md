# NEVI Plan Keyword Search Tool

This tool is designed to help analysts and researchers **search through state NEVI plans** for structured, consistent responses to critical questions. It allows users to identify where certain phrases, terms, or topics appear in all 52 state NEVI PDF submissions using structured, logic-based keyword matching.

Built with PyQt5 and bundled for Windows and Linux using PyInstaller.

---

## 📄 What It Does

- Load any individual state NEVI plan (PDF)
- Select from preset **equity**, **buildout**, and **maintenance** categories
- Each question contains sets of semantically related terms
- A page is matched if it contains **at least one term from each group**
- View matched pages with keywords **highlighted** in a scrollable reader
- Terms can be **edited directly** using the built-in JSON editor interface

---

## 🧱 Project Structure

```
.
├── main.py                        # App entry point
├── data/
│   └── terms.json                # Preset questions and keyword groups
├── assets/
│   └── wpi_logo.ico              # App icon
├── gui/
│   ├── main_window.py            # Main GUI window
│   ├── reader_window.py          # PDF reader with highlights
│   └── term_editor_window.py     # Editor for modifying keyword sets
├── logic/
│   ├── search_engine.py          # Keyword match logic
│   ├── term_loader.py            # Load files compatibly with PyInstaller
│   └── settings.py               # (Reserved for future use)
└── .github/workflows/windows-build.yml   # GitHub Actions for automatic .exe builds
```

---

## 🔍 Example Question

> **"How does the state identify disadvantaged communities?"**

```json
[
  ["underserved", "disadvantaged", "DAC", "marginalized"],
  ["define", "identify", "locate"],
  ["engagement", "collaboration", "mapping tool"]
]
```

This matches if a page contains **one term from each line**.

---

## ⚙️ Installation (Local)

```bash
pip install PyQt5 pypdf
python main.py
```

---

## 🏗️ Building the App (Linux)

Use PyInstaller to create a portable binary:

```bash
pyinstaller --onefile --windowed \
  --icon=assets/wpi_logo.ico \
  --add-data=data/terms.json:data \
  main.py
```

Output: `dist/main`

---

## 🚀 Automated Windows Builds via GitHub Actions

Create a release tag (`v1.0.0`) and GitHub will:
- Build a Windows `.exe`
- Upload it to the release automatically

```bash
git tag v1.0.0
git push origin v1.0.0
```

---

## 🧠 Background

This project was originally created as part of a WPI undergraduate research initiative in response to the **National Electric Vehicle Infrastructure (NEVI)** program, a federal effort to accelerate EV adoption.

The goal was to help teams quickly analyze large amounts of state-submitted content using structured keyword-driven search.

---

## ✍️ Authors

Originally developed by @nickborrello  
Supported by WPI research advisors  
Maintained and packaged by the research team
