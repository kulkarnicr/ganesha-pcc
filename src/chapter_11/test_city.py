# Ganesha# Ganesha
from city_functions import get_city_information, get_city_information_detailed


def test_positive_city_information():
    assert get_city_information('mumbai', 'India') == 'Mumbai, India'


def test_positive_city_information_detailed():
    assert get_city_information_detailed('mumbai', 'India', 1_00_000) == 'Mumbai, India - Population 100000'


def test_negative_city_information_detailed():
    assert get_city_information_detailed('mumbai', 'India') == 'Mumbai, India - Population 100000'
