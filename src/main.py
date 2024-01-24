from src.getting_data_from_the_api import HeadHunterAPI
from src.load_in_file import EXELload
from src.visualization import Graph
from src.make_new_structure import CreateJSON
from src.creating_vacancy import Vacancy
from src.data_base_region import SearchIdRegion


if __name__ == "__main__":
    print('Доброго времени суток! Выберите регион поиска работы')
    answer_user = input('Ваш регион: ')
    number_region = SearchIdRegion.get_id(answer_user)
    print(f'Регион поиска выбран, индекс: {number_region}')
    answer_user = input('Выберите специальность по которой желаете найти вакансии: ')
    vacancy_search = CreateJSON(answer_user, number_region, page=0)
