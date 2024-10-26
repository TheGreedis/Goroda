from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)
    if results:
        return results[0]['geometry']['lat'], results[0]['geometry']['lng']
    else:
        return "Город не найден"


key = 'eb19b70c52c14d06987345d9476cca7b'
city = "Moscow"
coordinates = get_coordinates(city, key)
print(f"Координаты гоорода {city}: {coordinates}")
