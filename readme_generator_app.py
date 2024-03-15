from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QPushButton,
                             QTextBrowser, QMessageBox, QFileDialog)
from typing import Optional
from readme_database import ReadmeDatabase


class ReadmeGeneratorApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        db: ReadmeDatabase = ReadmeDatabase()
        self.document_encoding: str = db.document_encoding

        self.setWindowTitle("README Generator")
        self.setGeometry(100, 100, 600, 600)

        self.project_name_label: QLabel = QLabel("Project Name:")
        self.project_name_entry: QLineEdit = QLineEdit()

        self.description: str = db.description_text
        self.description_label: QLabel = QLabel("Description:")
        self.description_entry: QTextEdit = QTextEdit(self.add_line_breaks(self.description))

        self.installation_label: QLabel = QLabel("Installation Instructions:")
        self.installation_entry: QTextEdit = QTextEdit()

        self.usage_label: QLabel = QLabel("Usage Examples:")
        self.usage_entry: QTextEdit = QTextEdit()

        self.author_information_text: str = db.author_information_text
        self.author_information_label: QLabel = QLabel("Author Information:")
        self.author_information_entry: QTextEdit = QTextEdit(self.add_line_breaks(self.author_information_text))
        self.author_information_entry.setFixedHeight(300)
        self.author_information_entry.setAcceptRichText(True)

        self.generate_button: QPushButton = QPushButton("Generate README")
        self.generate_button.clicked.connect(self.generate_readme)

        self.save_button: QPushButton = QPushButton("Save README")
        self.save_button.clicked.connect(self.save_readme)

        self.preview_label: QLabel = QLabel("Preview:")
        self.preview_text: QTextBrowser = QTextBrowser()

        layout: QVBoxLayout = QVBoxLayout()
        layout.addWidget(self.project_name_label)
        layout.addWidget(self.project_name_entry)
        layout.addWidget(self.description_label)
        layout.addWidget(self.description_entry)
        layout.addWidget(self.installation_label)
        layout.addWidget(self.installation_entry)
        layout.addWidget(self.usage_label)
        layout.addWidget(self.usage_entry)
        layout.addWidget(self.author_information_label)
        layout.addWidget(self.author_information_entry)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.preview_label)
        layout.addWidget(self.preview_text)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def generate_readme(self) -> None:
        project_name: str = self.project_name_entry.text()
        description: str = self.description_entry.toPlainText()
        installation: str = self.installation_entry.toPlainText()
        usage: str = self.usage_entry.toPlainText()
        author_information: str = self.author_information_entry.toPlainText()

        readme_content: str = (f"# {project_name}\n"
                               f"\n{description}\n"
                               f"\n{installation}\n"
                               f"\n{usage}\n"
                               f"\n{author_information}\n")

        self.preview_text.setPlainText(readme_content)

    def save_readme(self) -> None:
        filename: str
        _: Optional[str]
        filename, _ = QFileDialog.getSaveFileName(self, "Save README File", "README.md",
                                                  "Markdown Files (*.md);;Text Files (*.txt);;All Files (*)")
        if filename:
            try:
                with open(filename, 'w', encoding=self.document_encoding) as file:
                    file.write(self.preview_text.toPlainText())
                QMessageBox.information(self, "Success", "README saved successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    @staticmethod
    def add_line_breaks(text: str) -> str:
        return text.replace('\n', '<br>')
