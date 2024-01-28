from src.getting_data_from_the_api import HeadHunterAPI
from src.load_in_file import EXELload
from src.visualization import Graph
from src.make_new_structure import CreateJSON
from src.creating_vacancy import Vacancy
from src.data_base_region import SearchIdRegion

def dialog_with_user_about_vacancy_salary_gist() -> None:
    print('Доброго времени суток! Выберите регион поиска работы')
    answer_user = input('Ваш регион: ')
    number_region = SearchIdRegion.get_id(answer_user)
    print(f'Регион поиска выбран, индекс: {number_region}')
    specialization = input('Выберите специальность по которой желаете найти вакансии: ')
    vacancy_search = CreateJSON(name=specialization, region=number_region, page=0)
    js_obj = HeadHunterAPI.get_one_page_vacancies(name=specialization, region=number_region, page=0)["items"]
    for i in vacancy_search.create_new_struckt():
        print(f"Название специальности {i['Название специальности']}, Ссылка на объявление {i['Ссылка на объявление']},
              f"Зарплата от {i['Зарплата от']} Зарплата до {i['Зарплата до']} Требования к кандидату {i['Требования к кандидату']}")
    answer_user = input(f'Желаете ли Вы построить гистограмму заработных плат на специальность {specialization} Да/Нет ')
    match answer_user.lower():
        case 'да':
            df = EXELload.df_generate(js_obj)
            print('Выполняю...')
            Graph.draw_hist(df)
            print('До свидания')
        case 'нет':
            print('До свидания')

if __name__ == "__main__":
    pass
