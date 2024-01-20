from typing import Any
from unittest.mock import patch

import pytest
import requests

from src.data_base_region import SearchIdRegion


@pytest.mark.parametrize("error", [KeyError, ValueError, requests.exceptions.HTTPError])
@patch("requests.get")
def test_get_all_regions(mock_get: Any, error: Any) -> None:
    """Тестовая функция с имитацией ошибки"""
    mock_get.side_effect = error
    with pytest.raises(ValueError):
        assert SearchIdRegion.get_all_regions() == "Что-то пошло не так"


@pytest.mark.parametrize(
    "region, result", [("Москва", "1"), ("Челябинская область", "1384")]
)
def test_get_id(region: Any, result: Any') -> None:
    """тестовая функция получения ID"""
    assert SearchIdRegion.get_id(region) == result
    assert SearchIdRegion.get_id(region) == result
    with pytest.raises(ValueError):
        assert SearchIdRegion.get_id("пупкино") == "Регион не найден"
