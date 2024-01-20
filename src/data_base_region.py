from typing import Any

import requests


class SearchIdRegion:
    """Класс, который ищет айдишник региона"""

    russia_regions: str = (
        "https://api.hh.ru/areas/113"  # url для поиска айдишников российских регионов
    )

    @classmethod
    def get_all_regions(cls) -> list[Any]:
        """Данный метод возвращает json объект по всем регионам"""
        try:
            return requests.get(cls.russia_regions).json()
        except (requests.exceptions.HTTPError, ValueError, KeyError):
            raise ValueError("Что-то пошло не так")

    @classmethod
    def get_id(cls, name_region: str) -> str:
        for region in cls.get_all_regions()["areas"]:
            if region["name"] == name_region.capitalize():
                return region["id"]
        else:
            raise ValueError("Регион не найден")


if __name__ == "__main__":
    # print(SearchIdRegion.get_all_regions())
    print(SearchIdRegion.get_id("челябинская область"))
    print(SearchIdRegion.get_id("москва"))
