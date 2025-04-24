from PyQt5 import QtWidgets, QtGui, QtCore
import json
import os

class TermEditorWindow(QtWidgets.QWidget):
    def __init__(self, json_path="terms.json"):
        super().__init__()
        self.setWindowTitle("Term Editor")
        self.resize(800, 600)
        self.json_path = json_path
        self.data = {}

        self.load_json()

        # Layouts
        layout = QtWidgets.QVBoxLayout(self)

        # Top row: category dropdown + buttons
        cat_layout = QtWidgets.QHBoxLayout()
        self.cat_combo = QtWidgets.QComboBox()
        self.cat_combo.currentTextChanged.connect(self.load_questions)
        self.add_cat_btn = QtWidgets.QPushButton("Add Category")
        self.remove_cat_btn = QtWidgets.QPushButton("Remove Category")
        cat_layout.addWidget(self.cat_combo)
        cat_layout.addWidget(self.add_cat_btn)
        cat_layout.addWidget(self.remove_cat_btn)

        # Middle row: questions list + buttons
        ques_layout = QtWidgets.QVBoxLayout()
        self.question_list = QtWidgets.QListWidget()
        self.add_question_btn = QtWidgets.QPushButton("Add Question")
        self.remove_question_btn = QtWidgets.QPushButton("Remove Question")
        ques_layout.addWidget(self.question_list)
        ques_layout.addWidget(self.add_question_btn)
        ques_layout.addWidget(self.remove_question_btn)

        # Right row: terms editor
        terms_layout = QtWidgets.QVBoxLayout()
        self.terms_editor = QtWidgets.QPlainTextEdit()
        self.terms_editor.setPlaceholderText("Enter list of term groups, one group per line:\ne.g.\nstakeholders, community\nengage, outreach")
        terms_layout.addWidget(QtWidgets.QLabel("Term Groups (CSV per line):"))
        terms_layout.addWidget(self.terms_editor)

        # Bottom: save button
        self.save_btn = QtWidgets.QPushButton("Save Changes")

        # Final layout
        main_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(ques_layout, 2)
        main_layout.addLayout(terms_layout, 3)
        layout.addLayout(cat_layout)
        layout.addLayout(main_layout)
        layout.addWidget(self.save_btn)

        # Hooks
        self.add_cat_btn.clicked.connect(self.add_category)
        self.remove_cat_btn.clicked.connect(self.remove_category)
        self.add_question_btn.clicked.connect(self.add_question)
        self.remove_question_btn.clicked.connect(self.remove_question)
        self.question_list.itemClicked.connect(self.load_terms)
        self.save_btn.clicked.connect(self.save_terms)

        self.load_categories()

    def load_json(self):
        if os.path.exists(self.json_path):
            with open(self.json_path, "r") as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def save_json(self):
        with open(self.json_path, "w") as f:
            json.dump(self.data, f, indent=2)

    def load_categories(self):
        self.cat_combo.clear()
        self.cat_combo.addItems(sorted(self.data.keys()))
        if self.cat_combo.count() > 0:
            self.cat_combo.setCurrentIndex(0)
            self.load_questions()

    def load_questions(self):
        self.question_list.clear()
        cat = self.cat_combo.currentText()
        if cat in self.data:
            self.question_list.addItems(sorted(self.data[cat].keys()))

    def load_terms(self):
        cat = self.cat_combo.currentText()
        question = self.question_list.currentItem().text()
        groups = self.data[cat][question]
        lines = [", ".join(group) for group in groups]
        self.terms_editor.setPlainText("\n".join(lines))

    def save_terms(self):
        cat = self.cat_combo.currentText()
        question_item = self.question_list.currentItem()
        if not cat or not question_item:
            return
        question = question_item.text()
        lines = self.terms_editor.toPlainText().strip().splitlines()
        groups = [[term.strip() for term in line.split(",") if term.strip()] for line in lines if line.strip()]
        self.data[cat][question] = groups
        self.save_json()
        QtWidgets.QMessageBox.information(self, "Saved", f"Terms saved to {self.json_path}")

    def add_category(self):
        name, ok = QtWidgets.QInputDialog.getText(self, "New Category", "Category name:")
        if ok and name:
            if name not in self.data:
                self.data[name] = {}
                self.load_categories()
                self.cat_combo.setCurrentText(name)

    def remove_category(self):
        cat = self.cat_combo.currentText()
        if cat and cat in self.data:
            del self.data[cat]
            self.load_categories()

    def add_question(self):
        cat = self.cat_combo.currentText()
        if not cat:
            return
        name, ok = QtWidgets.QInputDialog.getText(self, "New Question", "Question:")
        if ok and name:
            if name not in self.data[cat]:
                self.data[cat][name] = []
                self.load_questions()

    def remove_question(self):
        cat = self.cat_combo.currentText()
        item = self.question_list.currentItem()
        if cat and item:
            del self.data[cat][item.text()]
            self.load_questions()
