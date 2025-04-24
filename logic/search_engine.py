from pypdf import PdfReader
import re

def group_matches(text, group):
    for term in group:
        if term.strip() == "":
            continue
        pattern = r"\b" + re.escape(term) + r"\b"
        if re.search(pattern, text, flags=re.IGNORECASE):
            return True
    return False

def search_pdf_for_terms(pdf_path, term_sets):
    results = {}
    reader = PdfReader(pdf_path)

    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        lower_text = text.lower()
        if all(group_matches(lower_text, group) for group in term_sets):
            results[i] = text

    return results
