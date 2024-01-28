import re
from operator import itemgetter
from typing import Generator

from src.creating_vacancy import Vacancy
from src.data_base_region import SearchIdRegion
from src.getting_data_from_the_api import HeadHunterAPI
from src.load_in_file import EXELload
from src.make_new_structure import CreateJSON
from src.visualization import Graph


def filter_vacancies(hh_vacancies: list, filter_words: str) -> list:
    """Функция фильтрации вакансии по ключевому слову, поиск ведётся в требованиях к кандидату"""
    for i in hh_vacancies:
        try:
            if re.findall(
                r"\b({})\b".format(filter_words), i["Требования к кандидату"]
            ):
                yield i
        except TypeError:
            continue


def sort_vacancies(filtered_vacancies: Generator) -> list:
    """Функция сортировки по зарплате"""
    return sorted(list(filtered_vacancies), key=itemgetter("Зарплата от"))


def get_top_vacancies(sorted_vacancies: list, top_n: int) -> list:
    """Функция возвращает список топ вакансий"""
    return sorted_vacancies[:top_n]


def dialog_with_user_about_vacancy_salary_gist() -> None:
    print("Доброго времени суток! Выберите регион поиска работы")
    answer_user = input("Ваш регион: ")
    number_region = SearchIdRegion.get_id(answer_user)
    print(f"Регион поиска выбран, индекс: {number_region}")
    specialization = input("Выберите специальность по которой желаете найти вакансии: ")
    vacancy_search = CreateJSON(name=specialization, region=number_region, page=0)
    js_obj = HeadHunterAPI.get_one_page_vacancies(
        name=specialization, region=number_region, page=0
    )["items"]
    for i in vacancy_search.create_new_struckt():
        print(
            f"""Название специальности {i['Название специальности']}, Ссылка на объявление {i['Ссылка на объявление']},
              Зарплата от {i['Зарплата от']} Зарплата до {i['Зарплата до']} Требования к кандидату {i['Требования к кандидату']}"""
        )
    answer_user = input(
        f"Желаете ли Вы построить гистограмму заработных плат на специальность {specialization} Да/Нет "
    )
    match answer_user.lower():
        case "да":
            df = EXELload.df_generate(js_obj)
            print("Выполняю...")
            Graph.draw_hist(df)
            print("До свидания")
        case "нет":
            print("До свидания")


def print_vacancies(top_vacancies: list) -> None:
    for i in top_vacancies:
        print(i)


def user_interaction(hh_vacancies: list) -> None:
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ")
    filtered_vacancies = filter_vacancies(hh_vacancies, filter_words)
    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    # Создание двух экземпляров класса, CreateJSON и HeadHunterAPI
    hh_api = CreateJSON("снабжение", "1384", 0)
    # Создание экземпляра класса Vacancy
    vacancy = Vacancy(
        "машинист", "www.hh.ru/vacancy/12543513", "5000-1000 руб", "Быть весёлым"
    )
    # Добавляем вакансию в новую структуру и сразу же записываем json файл
    CreateJSON.add_vacancy(vacancy)
    # Создаем новую структуру полученных вакансий от hh.ru и до записываем их в json файл
    hh_api.create_new_struckt()
    print(hh_api.vacancy_list)
    # удаление вакансии и обновление json'а
    CreateJSON.remove_vacancy(vacancy)
    print(hh_api.vacancy_list)
    user_interaction(hh_api.vacancy_list)
