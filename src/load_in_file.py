from abc import ABC, abstractmethod
import pandas as pd
from src.getting_data_from_the_api import HeadHunterAPI
import pathlib


class Example(ABC):

    @staticmethod
    @abstractmethod
    def df_generate(any_json: dict):
        pass

    @staticmethod
    @abstractmethod
    def load_in_exel_file():
        pass


class EXELload(Example):
    """Класс формирующий данные в Датафрейм и загружает их в Exel файл"""

    @staticmethod
    def df_generate(any_json: dict):
        """Метод формирует дата фрейм из json"""
        df = pd.DataFrame(any_json["items"])
        return df

    @classmethod
    def load_in_exel_file(cls, any_json: dict=None):
        """Загружаем файлы в Exel file"""
        df = cls.df_generate(any_json)
        with pd.ExcelWriter(pathlib.Path.home().joinpath('report_vacancies.xlsx')) as writer_obj:
            df.to_excel(writer_obj, sheet_name='Вакансии')


if __name__ == '__main__':
    js_obj = HeadHunterAPI.get_one_page_vacancies('снабжение', '1384', 0)
    EXELload.load_in_exel_file(js_obj)

