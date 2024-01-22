import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from src.load_in_file import EXELload
from src.getting_data_from_the_api import HeadHunterAPI


class Graph:
    @staticmethod
    def draw_hist(dataframe: pd.DataFrame) -> None:
        """Метод, для визуального отображения заработных плат(Гистограмма)"""
        df = EXELload.get_salary(data_frame=dataframe)
        # # Создание гистограммы
        df.hist(bins=50)
        # Отображение гистограммы
        plt.savefig("Гистограмма заработных плат.png")
    @staticmethod
    def draw(dataframe: pd.DataFrame):
        """Метод, для визуального отображения заработных плат(график)"""
        df = EXELload.get_salary(data_frame=dataframe)
        df['Index'] = np.arange(len(df))
        # Создание графика
        plt.plot(df['Index'], df['from'])
        plt.plot(df['Index'], df['to'])
        plt.ylabel('Salary')
        plt.xlabel('Index')
        plt.title('Salary vs. Index')
        plt.savefig("График заработных плат.png")

if __name__ == '__main__':
    js_obj = HeadHunterAPI.get_one_page_vacancies("снабжение", "1384", 0)
    df = EXELload.df_generate(js_obj)
    Graph.draw_hist(df)
    # Graph.draw(df)
