import pathlib
from abc import ABC, abstractmethod
from typing import Any, Optional

import pandas as pd

from src.getting_data_from_the_api import HeadHunterAPI


class Example(ABC):
    @staticmethod
    @abstractmethod
    def df_generate(any_json: dict):
        pass

    @staticmethod
    @abstractmethod
    def load_in_exel_file(path_file, any_json):
        pass


class EXELload(Example):
    """Класс формирующий данные в Датафрейм и загружает их в Exel файл"""

    @staticmethod
    def df_generate(any_json: dict) -> pd.DataFrame:
        """Метод формирует дата фрейм из json"""
        df = pd.DataFrame(any_json["items"])
        return df

    @classmethod
    def load_in_exel_file(cls, path_file: Any, any_json: Optional) -> None:
        """Загружаем файлы в Exel file"""
        df = cls.df_generate(any_json)
        with pd.ExcelWriter(path_file) as writer_obj:
            df.to_excel(writer_obj, sheet_name="Вакансии")

    @staticmethod
    def get_salary(data_frame: pd.DataFrame) -> pd.DataFrame:
        """Метод получения всех зарплат"""
        salary: list = [d for d in data_frame['salary'] if d is not None]
        return pd.DataFrame(salary)


if __name__ == "__main__":
    # path_file = pathlib.Path.home().joinpath("report_vacancies.xlsx")
    js_obj = HeadHunterAPI.get_one_page_vacancies("снабжение", "1384", 0)
    # EXELload.load_in_exel_file(path_file, js_obj)
    df = EXELload.df_generate(HeadHunterAPI.get_one_page_vacancies("снабжение", "1384", 0))
    # print(js_obj["items"])
    # print(type(df))
    print(EXELload.get_salary(data_frame=df))




