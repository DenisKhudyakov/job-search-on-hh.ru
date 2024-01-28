import functools
import json
from copy import copy
from typing import Callable, Optional

from src.creating_vacancy import Vacancy
from src.getting_data_from_the_api import HeadHunterAPI


class CreateJSON:

    """Класс, создания json объекта и записи в json файл"""

    vacancy_list = []
    new_struct = {
        "Название специальности": None,
        "Ссылка на объявление": None,
        "Зарплата от": None,
        "Зарплата до": None,
        "Требования к кандидату": None,
    }

    def __init__(self, name: str, region: str, page: int) -> None:
        self.api = HeadHunterAPI.get_one_page_vacancies(name, region, page)

    @staticmethod
    def write_json(func: Callable) -> Optional:
        """Декоратор записи данных в Json файл"""

        @functools.wraps(func)
        def inner(*args, **kwargs) -> list:
            with open("vacancy.json", "a", encoding="UTF-8") as f:
                result = func(*args, **kwargs)
                json.dump(result, f, ensure_ascii=False, indent=4)
            return result

        return inner

    @staticmethod
    def re_write_json(func: Callable) -> Optional:
        """Декоратор перезаписи записи данных в Json файл"""

        @functools.wraps(func)
        def inner(*args, **kwargs) -> list:
            with open("vacancy.json", "w", encoding="UTF-8") as f:
                result = func(*args, **kwargs)
                json.dump(result, f, ensure_ascii=False, indent=4)
            return result

        return inner

    @write_json
    def create_new_struckt(self) -> list:
        """Преобразование ответа от API под предпочитаемую структуру"""
        for i_job in self.api["items"]:
            try:
                new_struct = copy(self.new_struct)
                new_struct["Название специальности"] = i_job["name"]
                new_struct["Ссылка на объявление"] = i_job["apply_alternate_url"]
                new_struct["Зарплата от"] = i_job["salary"]["from"]
                new_struct["Зарплата до"] = i_job["salary"]["to"]
                new_struct["Требования к кандидату"] = i_job["snippet"]["requirement"]
                self.vacancy_list.append(new_struct)
            except TypeError:
                continue
        return self.vacancy_list

    @classmethod
    def new_dict(cls, vacancy: Optional) -> dict:
        """Преобразование экземпляра класса Вакансия, в словарь другого формата"""
        salary_from, salary_to = vacancy.split_salary(vacancy.get_salary)
        new_struct = copy(cls.new_struct)
        new_struct["Название специальности"] = vacancy.get_name
        new_struct["Ссылка на объявление"] = vacancy.get_url
        new_struct["Зарплата от"] = salary_from
        new_struct["Зарплата до"] = salary_to
        new_struct["Требования к кандидату"] = vacancy.get_requirements
        return new_struct

    @classmethod
    @write_json
    def add_vacancy(cls, vacancy: Optional) -> list:
        """Метод добавления созданной вакансии"""
        new_struct = cls.new_dict(vacancy)
        cls.vacancy_list.append(new_struct)
        return cls.vacancy_list

    @classmethod
    @re_write_json
    def remove_vacancy(cls, vacancy: Optional) -> list:
        """Функция, которая удаляет записанный экземпляр класса"""
        new_struct = cls.new_dict(vacancy)
        cls.vacancy_list.remove(new_struct)
        return cls.vacancy_list


if __name__ == "__main__":
    api1 = CreateJSON("снабжение", "1384", 0)
    vacancy = Vacancy(
        "машинист", "www.hh.ru/vacancy/12543513", "5000-1000 руб", "Быть весёлым"
    )
    CreateJSON.add_vacancy(vacancy)
    api1.create_new_struckt()
    print(api1.vacancy_list)
    CreateJSON.remove_vacancy(vacancy)
    print(api1.vacancy_list)
