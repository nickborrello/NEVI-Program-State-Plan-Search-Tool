# Universal PDF Keyword Search Tool

A Python-based tool to search for structured keyword patterns in any PDF document — with visual highlights, page navigation, and full keyword management.

Originally built to explore NEVI state plans, now generalized for any use case involving keyword analysis in PDFs.

---

## 🚀 Features

- Load any PDF file
- Structured keyword matching (multi-group logic)
- Whole-word and case-insensitive search (no false positives)
- Highlighted reader view with page-by-page navigation
- JSON-based keyword sets (organized by category and question)
- Term editor for live editing and saving new keyword logic

---

## 🧱 Project Structure

```
NEVI-Program-State-Plan-Search-Tool/
├── main.py                        # Entry point
├── gui/
│   ├── main_window.py             # Main application UI
│   ├── reader_window.py           # PDF viewer with term highlighting
│   └── term_editor_window.py      # UI for editing term groups
├── logic/
│   ├── search_engine.py           # Keyword match engine using whole-word regex
│   └── term_loader.py             # Loads and parses terms.json
├── data/
│   └── terms.json                 # Sample term structure (editable)
```

---

## ⚙️ Installation

### Requirements

- Python 3.7+
- PyQt5
- pypdf

Install dependencies:

```bash
pip install PyQt5 pypdf
```

---

## 🧠 How It Works

### JSON Structure

`terms.json` contains a mapping like:

```json
{
  "Category Name": {
    "Some Question?": [
      ["group1_term1", "group1_term2"],
      ["group2_term1", "group2_term2"]
    ]
  }
}
```

A PDF page matches a question **only if at least one term from each group is found** on the page (AND logic across groups).

---

## 📦 Best Practices

- Keep your `terms.json` modular — avoid hardcoding terms into Python.
- Use the **term editor** to safely update/add categories and questions.
- Maintain backups of your `terms.json` if editing outside the UI.
- Stick to **simple lowercase, whole-word terms** for most accurate matching.
- Use an empty string (`" "`) in a group to make it optional.

---

## 🖥️ Running the App

```bash
python main.py
```

1. Load a PDF.
2. Select a category and question.
3. Click **Run Search**.
4. View matching pages in a popup reader with highlighted hits.

---

## ✅ TODO / Future Features

- Semantic search with vector embeddings
- Export matched pages as new annotated PDF
- Batch processing of PDF folders
- Plugin hooks for alternate match engines (e.g., fuzzy, AI)

---

## 🧑‍💻 Author

Refactored and maintained by @nickborrello  
Originally built for structured NEVI document analysis.
