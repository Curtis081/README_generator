import pytest
from datetime import datetime
from readme_database import ReadmeDatabase


@pytest.fixture
def readme_database():
    return ReadmeDatabase()


class TestReadmeDatabase:
    def test_format_current_datetime_as_string(self, readme_database):
        current_datetime = datetime.now()
        expected_date = current_datetime.strftime("%B %d, %Y")
        assert readme_database.format_current_datetime_as_string() == expected_date

    def test_description_text(self, readme_database):
        assert readme_database.description_text.startswith("\n            ## Introduction(簡介)\n\n")
        assert "Insert documentation here" in readme_database.description_text

    def test_author_information_text(self, readme_database):
        assert readme_database.author_information_text.startswith("## Author Information")
        assert "Curtis Hsu(Ying-Hao Hsu)" in readme_database.author_information_text
        assert readme_database.format_current_datetime_as_string() in readme_database.author_information_text
        assert "ar06053127hga@hotmail.com.tw" in readme_database.author_information_text
        assert "https://github.com/Curtis081" in readme_database.author_information_text
        assert "https://www.linkedin.com/in/yinghaohsu/" in readme_database.author_information_text

