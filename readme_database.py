from datetime import datetime


class ReadmeDatabase:
    def __init__(self) -> None:
        self.document_encoding: str = 'utf-8'
        self.description_text: str = (
            '''
            ## Introduction(簡介)\n
            \n
            {description}\n
            \n
            '''.format(description="Insert documentation here")
        )

        self.author_information_text: str = (
            '''## Author Information\n
            \n
            ### Name\n
            {author_name}\n
            \n
            ### Creation Date\n
            {current_date}\n
            \n
            ### Contact Information\n
            - **Email**: {email_address}\n
            - **GitHub**: [{github_name}]({github_link})\n
            - **LinkedIn**: [{linkedin_name}]({linkedin_link})\n
            \n
            #### Note\n
            For any inquiries or contributions regarding this project, 
            please feel free to contact me through the above channels. 
            If reporting bugs or requesting features, 
            consider opening an issue on GitHub for public tracking and documentation.\n
            '''.format(
                    author_name="Curtis Hsu(Ying-Hao Hsu)",
                    current_date=self.format_current_datetime_as_string(),
                    email_address="ar06053127hga@hotmail.com.tw",
                    github_name="Curtis081",
                    github_link="https://github.com/Curtis081",
                    linkedin_name="Curtis Hsu(Ying-Hao Hsu)",
                    linkedin_link="https://www.linkedin.com/in/yinghaohsu/"
                )
            )

    @staticmethod
    def format_current_datetime_as_string() -> str:
        current_datetime: datetime = datetime.now()
        formatted_date: str = current_datetime.strftime("%B %d, %Y")
        return formatted_date
