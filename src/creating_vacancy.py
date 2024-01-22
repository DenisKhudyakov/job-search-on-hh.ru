from abc import ABC, abstractmethod

from src.load_in_file import EXELload


class AbstractVacancy(ABC):
    @abstractmethod
    def __init__(self, name: str, url: str, salary: str, requirements: str) -> None:
        pass

    @abstractmethod
    def __dict__(self):
        pass


class Vacancy:
    """Класс вакансия, создает новую вакансию экземпляр данного класса будет
    в формате json, необходимо определить метод __dict__"""

    def __init__(self, name: str, url: str, salary: str, requirements: str) -> None:
        """Конструктор класса Вакансия, параметры название, электронный адрес, зарплата, требования к кандидату"""
        self.name = name
        self.url = url
        self.salary = salary
        self.requirements = requirements

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
        return {
            "items": [
                {
                    "name": self.name,
                    "url": self.url,
                    "salary": self.salary,
                    "responsibility": self.requirements,
                }
            ]
        }


if __name__ == "__main__":
    print(
        EXELload.df_generate(Vacancy("gdsfg", "gsdfg", "gsfdg", "gsdfgfg").__dict__())
    )
