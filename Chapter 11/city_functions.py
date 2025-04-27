def formatted_location(city_name, country_name, population=''):
    if population:
        formatted_place = f"{country_name}, {city_name}: {population}"
    else:
        formatted_place = f"{country_name}, {city_name}"
    return formatted_place.title()
