# Ganesha
"""source code python file to provide city relation functions"""

def get_city_information(city, country):
    """get city and country"""
    
    return f"{city}, {country}".title()


def get_city_information_detailed(city, country, population):
    """get city and country with population"""
    
    return f"{city}, {country} - population {population}".title()