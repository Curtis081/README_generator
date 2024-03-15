import pytest
from readme_generator_app import ReadmeGeneratorApp
from pytestqt.qt_compat import qt_api


@pytest.fixture
def readme_generator_app(qtbot):
    readme_generator = ReadmeGeneratorApp()
    qtbot.addWidget(readme_generator)
    return readme_generator


class TestReadmeGeneratorApp:
    def test_add_line_breaks(self, readme_generator_app):
        text = "Line1\nLine2\nLine3"
        expected_output = "Line1<br>Line2<br>Line3"
        assert readme_generator_app.add_line_breaks(text) == expected_output

    def test_generate_readme(self, readme_generator_app, qtbot):
        app = readme_generator_app
        app.project_name_entry.setText('Test Project')
        app.description_entry.setPlainText('This is a test description.')
        app.installation_entry.setPlainText('pip install test')
        app.usage_entry.setPlainText('python test.py')
        app.author_information_entry.setPlainText('lucky person')

        qtbot.addWidget(app.generate_button)
        qtbot.mouseClick(app.generate_button, qt_api.QtCore.Qt.MouseButton.LeftButton)

        expected_readme_content = ("# Test Project\n"
                                   "\nThis is a test description.\n"
                                   "\npip install test\n"
                                   "\npython test.py\n"
                                   "\nlucky person\n")
        assert app.preview_text.toPlainText() == expected_readme_content
