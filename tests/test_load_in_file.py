import os
import pathlib
import unittest

from src.getting_data_from_the_api import HeadHunterAPI
from src.load_in_file import EXELload


class TestCreateFile(unittest.TestCase):
    def test_load_in_exel_file(self) -> None:
        file_path = pathlib.Path.home().joinpath("report_vacancies.xlsx")
        json_obj = HeadHunterAPI.get_one_page_vacancies("снабжение", "1384", 0)
        EXELload.load_in_exel_file(file_path, json_obj)

        self.assertTrue(os.path.exists(file_path))
        self.assertTrue(os.path.isfile(file_path))

        os.remove(file_path)
        self.assertFalse(os.path.exists(file_path))


if __name__ == "__main__":
    unittest.main()
