def __init__(self):
    super().__init__()
    self.setWindowTitle("Universal PDF Keyword Search")
    self.resize(1000, 700)
    self.terms = {}
    self.selected_file = None

    self.setup_ui()
    self.load_terms_file("data/terms.json")  # auto-load default terms
