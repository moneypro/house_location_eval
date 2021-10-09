from house_location_eval import HouseLocationEval
import sys
from typing import List

def read_from_house_location_txt():
    # type: () -> None
    with open("./house_location.txt") as f:
        house_location_list = [non_empty_line for non_empty_line in [line.strip() for line in f.readlines()] if
                               non_empty_line != ""]
    evaluator = HouseLocationEval()
    evaluator.eval(house_location_list)


def read_from_command_line(house_location_list):
    # type: (List[str]) -> None
    evaluator = HouseLocationEval()
    evaluator.eval(house_location_list)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        read_from_house_location_txt()
    read_from_command_line(sys.argv[1:])
