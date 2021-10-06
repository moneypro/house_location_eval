import googlemaps
from googlemaps.directions import directions
from _datetime import datetime, timezone, timedelta

with open("./google_api.secret") as f:
    google_api_key = f.readline()

gmaps = googlemaps.Client(key=google_api_key)
house_location_list = [
    "22928 NE 15th Pl Sammamish, WA 98074",
    "4932 125th Ave SE Bellevue, WA 98006",
    "6009 147th Ave SE Bellevue, WA 98006",
    "4429 233rd Pl SE Bothell, WA 98021"
]
now = datetime.now()
morning = datetime(now.year, now.month, now.day + 1, 8, 0, 0, tzinfo=timezone(timedelta(hours=-8)))
afternoon = datetime(now.year, now.month, now.day + 1, 15, 0, 0, tzinfo=timezone(timedelta(hours=-8)))
# night also represents off hours / weekends
night = datetime(now.year, now.month, now.day + 1, 21, 0, 0, tzinfo=timezone(timedelta(hours=-8)))
frequent_places_departure_time = {
    "Jing Mei": ("HR2H+WJ Bellevue, Washington", [morning, afternoon]),
    "Asian Family Market Bellevue": ("JVG3+P9 Bellevue, Washington", [morning, afternoon, night]),
    "Bellevue Square": ("JQ8W+79 Bellevue, Washington", [night]),
}
for house_location in house_location_list:
    print("House location: {}".format(house_location))
    for destination_name, destination_data in frequent_places_departure_time.items():
        destination_location, time_to_departure_list = destination_data
        print("Destination: {}".format(destination_name))
        for time_to_departure in time_to_departure_list:
            directions_result = directions(client=gmaps, origin=house_location, destination=destination_location,
                                           departure_time=time_to_departure)
            if len(directions_result) == 0:
                print("When departure at {}：00, no data is available.".format(time_to_departure.hour))
            print("When departure at {}:00, takes {} and the distance is {}.".format(
                time_to_departure.hour,
                directions_result[0]['legs'][0]['duration_in_traffic']['text'],
                directions_result[0]['legs'][0]['distance']['text']))
    print("----------------")
