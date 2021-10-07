from collections import defaultdict


class DestinationResult:
    def __init__(self, origin):
        self.origin = origin
        self.directions = defaultdict(lambda: defaultdict(list))
        self.destination_to_destination_name_map = dict()

    def add(self, destination_name, destination, hour, google_map_directions_result):
        self.directions[destination][hour].append(google_map_directions_result)
        self.destination_to_destination_name_map[destination] = destination_name

    def to_string(self):
        res = "House location: {}".format(self.origin)
        for destination, destination_data in self.directions:
            res += ("Destination: {}".format(self.destination_to_destination_name_map[destination]))
            for hour, directions_result in destination_data:
                res += "When departure at {}:00, takes {} and the distance is {}.".format(
                    hour,
                    directions_result[0]['legs'][0]['duration_in_traffic']['text'],
                    directions_result[0]['legs'][0]['distance']['text'])
        return res
