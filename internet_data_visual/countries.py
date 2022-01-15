from pygal.maps.world import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(f'"{country_code}", "{COUNTRIES[country_code]}"')
