import json
from abc import ABC, abstractmethod

import requests

# param = {'page': 1, 'per_page': 100, 'text': 'NAME:снабжение', 'area': '1384'}
#
# url = 'https://api.hh.ru/vacancies'


# response = requests.get(url, params=param)
# for i in response.json()['items']:
#     print(i)
class PatternClassForWorkWithAPI(ABC):
    """Абстрактный класс для работы с АПИ"""

    @classmethod
    @abstractmethod
    def get_one_page_vacancies(cls, name: str, region: str, page: int):
        pass


class HeadHunterAPI(PatternClassForWorkWithAPI):
    url: str = "https://api.hh.ru/vacancies"

    @classmethod
    def get_one_page_vacancies(cls, name: str, region: str, page: int) -> str:
        """Функция получения вакансий по названию профессии"""
        param = {"page": page, "per_page": 100, "text": f"NAME:{name}", "area": region}
        return requests.get(cls.url, params=param).json()


if __name__ == "__main__":
    print(HeadHunterAPI.get_one_page_vacancies("снабжение", "1384", 0)['items'])
