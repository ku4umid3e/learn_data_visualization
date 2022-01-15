from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """ Returns its two-letter Pygal code for a given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If the country is not found return None.
    return None
