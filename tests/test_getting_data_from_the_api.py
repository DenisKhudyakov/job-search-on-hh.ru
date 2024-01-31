import unittest

from src.getting_data_from_the_api import HeadHunterAPI


class TestGetData(unittest.TestCase):
    def test_get_one_page_vacancies(self):
        data = HeadHunterAPI.get_one_page_vacancies("снабжение", "1384", 0)
        self.assertIsNotNone(data)
        self.assertIsInstance(data, dict)


if __name__ == "__main__":
    unittest.main()
