import requests


class DataSource:
    INFOGRAM = 'https://e.infogram.com/f7ef47cc-89ac-4979-ba62-6e9621526338'

    @staticmethod
    def get_infogram_content() -> str:
        response = requests.get(DataSource.INFOGRAM)
        return response.text
