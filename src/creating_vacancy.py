from abc import ABC, abstractmethod

from src.load_in_file import EXELload

import pandas as pd


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


if __name__ == "__main__":
    any_dict = Vacancy("gdsfg", "gsdfg", "gsfdg", "gsdfgfg")
    any_dict1 = Vacancy("gdsfg1", "gsdfg", "gsfdg", "gsdfgfg")
    print(any_dict.df_generate())