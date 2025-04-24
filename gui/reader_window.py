from PyQt5 import QtWidgets, QtGui, QtCore
from pypdf import PdfReader

class ReaderWindow(QtWidgets.QWidget):
    def __init__(self, pdf_path, matched_pages, term_sets, parent=None):
        super().__init__(parent)
        self.setWindowTitle("PDF Viewer - Highlighted Matches")
        self.resize(800, 600)

        self.pdf_path = pdf_path
        self.matched_pages = matched_pages
        self.term_sets = term_sets
        self.current_index = 0

        self.reader = PdfReader(self.pdf_path)

        layout = QtWidgets.QVBoxLayout(self)
        self.text_viewer = QtWidgets.QTextEdit(self)
        self.text_viewer.setReadOnly(True)
        self.text_viewer.setFont(QtGui.QFont("Arial", 12))
        layout.addWidget(self.text_viewer)

        nav_layout = QtWidgets.QHBoxLayout()
        self.prev_button = QtWidgets.QPushButton("Previous Page")
        self.next_button = QtWidgets.QPushButton("Next Page")
        self.page_label = QtWidgets.QLabel()
        nav_layout.addWidget(self.prev_button)
        nav_layout.addWidget(self.page_label, alignment=QtCore.Qt.AlignCenter)
        nav_layout.addWidget(self.next_button)
        layout.addLayout(nav_layout)

        self.prev_button.clicked.connect(self.prev_page)
        self.next_button.clicked.connect(self.next_page)

        self.update_page()

    def update_page(self):
        if not self.matched_pages:
            self.text_viewer.setPlainText("No matches found.")
            self.page_label.setText("Page: N/A")
            return

        page_num = self.matched_pages[self.current_index]
        page = self.reader.pages[page_num]
        text = page.extract_text() or ""

        self.highlight_text(text, self.term_sets)
        self.page_label.setText(f"Page: {page_num + 1}")

        self.prev_button.setEnabled(self.current_index > 0)
        self.next_button.setEnabled(self.current_index < len(self.matched_pages) - 1)

    def highlight_text(self, text, term_sets):
        self.text_viewer.setPlainText(text)
        cursor = self.text_viewer.textCursor()
        fmt = QtGui.QTextCharFormat()
        fmt.setBackground(QtGui.QColor("yellow"))

        for group in term_sets:
            for term in group:
                if not term.strip():
                    continue
                pattern = QtCore.QRegExp(r"\b" + QtCore.QRegExp.escape(term) + r"\b", QtCore.Qt.CaseInsensitive)
                pos = 0
                while (pos := pattern.indexIn(text, pos)) != -1:
                    cursor.setPosition(pos)
                    cursor.movePosition(QtGui.QTextCursor.EndOfWord, 1)
                    cursor.mergeCharFormat(fmt)
                    pos += pattern.matchedLength()

    def next_page(self):
        if self.current_index < len(self.matched_pages) - 1:
            self.current_index += 1
            self.update_page()

    def prev_page(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.update_page()
