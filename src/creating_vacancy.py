from abc import ABC, abstractmethod

import pandas as pd

from src.load_in_file import EXELload


class AbstractVacancy(ABC):
    @abstractmethod
    def __init__(self, name: str, url: str, salary: str, requirements: str) -> None:
        pass

    @abstractmethod
    def __dict__(self):
        pass


class Vacancy(AbstractVacancy):
    """Класс вакансия, создает новую вакансию экземпляр данного класса будет
    в формате json, необходимо определить метод __dict__"""

    __slots__ = ["name", "url", "salary", "requirements"]
    collect = []

    def __init__(self, name: str, url: str, salary: str, requirements: str) -> None:
        """Конструктор класса Вакансия, параметры название, электронный адрес, зарплата, требования к кандидату"""
        self.name = name
        self.url = url
        self.salary = salary
        self.requirements = requirements
        self.collect.append(self.__dict__())

    # Описываем геттеры всех параметров
    @property
    def get_name(self) -> str:
        return self.name

    @property
    def get_url(self) -> str:
        return self.url

    @property
    def get_salary(self) -> str:
        return self.salary

    @property
    def get_requirements(self) -> str:
        return self.requirements

    def __dict__(self):
        """Переопределяем метод словарь"""
        return {
            "name": self.name,
            "url": self.url,
            "salary": self.salary,
            "responsibility": self.requirements,
        }

    def df_generate(self) -> pd.DataFrame:
        """Метод который записывает все созданные экземпляры классов в ДатаФрейм"""
        return pd.DataFrame(self.collect)

    @staticmethod
    def split_salary(salary: str) -> tuple:
        """
        Функция которая преобразует формат зарплаты в
        Было: 1500-2000 руб
        Стало: (1500, 2000)
        """
        list_salary = salary.split("-")
        salary_to = list_salary[1].split()[0]
        return int(list_salary[0]), int(salary_to)

    @classmethod
    def filter_need_salary(cls, need_salary: int):
        """Функция определяет валидная ли вакансия, под заданную зарплату"""
        return list(
            filter(
                lambda salary: cls.split_salary(salary["salary"])[0]
                <= need_salary
                <= cls.split_salary(salary["salary"])[1],
                cls.collect,
            )
        )


if __name__ == "__main__":
    any_dict = Vacancy("Бухгалтер", "gsdfg", "1500-2000 руб", "Быть крутым работником")
    any_dict1 = Vacancy("Машинист", "gsdfg", "5000-6000 руб", "Мало спать")
    # print(any_dict.df_generate())
    print(Vacancy.filter_need_salary(need_salary=5000))
