#AIzaSyAp7mXYP0bVgywM4FGG6v4y5YJVmskQ0wk
from googleplaces import GooglePlaces
import webbrowser

#Программа выполняет поиск организаций в казани по ключевому слову и выводит их адреса
YOUR_API_KEY = 'AIzaSyAp7mXYP0bVgywM4FGG6v4y5YJVmskQ0wk'

google_places = GooglePlaces(YOUR_API_KEY)

keyword = input('Введите название организации: \n')

query_result = google_places.nearby_search(
        location='Kazan, Russia', keyword=keyword,
        radius=20000)

for place in query_result.places:
    print(place.name)
    place.get_details()
    print(place.formatted_address)
    webbrowser.open(place.url)

