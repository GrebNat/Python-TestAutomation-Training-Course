from collections import defaultdict

import pytest

from bad import create_country_make_dict as bad_dict
from good import create_country_make_dict as good_dict

REQUEST_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json"
actual_dictionary = defaultdict(set)


@pytest.mark.parametrize("dict_func", [bad_dict, good_dict])
def test_dict_length(dict_func):
    dict_length = len(dict_func(REQUEST_URL))
    assert dict_length == 79, f"Expected length to be 79, but got {dict_length} instead"


@pytest.mark.parametrize("country,expected_cities", [
    ("BRAZIL", {'BUSSCAR ONIBUS S.A.'}),
    ("TAIWAN", {'MOTIVE POWER INDUSTRY CO. LTD.', 'YAMAHA MOTOR TAIWAN CO., LTD.'})])
def test_cities_list(country, expected_cities):
    assert good_dict(REQUEST_URL)[country] == expected_cities, f"Expected cities to be {expected_cities}, but was not"


def test_countries_are_not_sorted():
    keys = good_dict(REQUEST_URL).keys()
    assert sorted(keys) != keys, "Expected list of countries is not sorted"
