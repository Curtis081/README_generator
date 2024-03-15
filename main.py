from PyQt6.QtWidgets import QApplication
import sys

from readme_generator_app import ReadmeGeneratorApp


def main() -> None:
    app: QApplication = QApplication(sys.argv)
    readme_app: ReadmeGeneratorApp = ReadmeGeneratorApp()
    readme_app.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
