from typing import Dict, List, Tuple

from pathlib import Path
import yaml
from yaml.loader import SafeLoader

class Cargo(object):
    #
    # Stores information about a single cargo item. The cargo item has a name, a weight in kg, and dimensions in meters.
    #

    CARGO_MAX_WEIGHT_IN_KG = 200
    CARGO_MAX_VOLUME_IN_M3 = 2.0

    def __init__(self, name: str, weight_in_kg: float, length_in_m: float, width_in_m: float, height_in_m: float):
        if name is None or name == "" or name.isspace():
            raise ValueError("Name of cargo item cannot be empty.")

        if weight_in_kg <= 0:
            raise ValueError(f"Weight of cargo item {name} must be greater than 0. The specified weight is {weight_in_kg}kg.")

        if weight_in_kg > Cargo.CARGO_MAX_WEIGHT_IN_KG:
            raise ValueError(f"Weight of cargo item {name} exceeds the maximum weight of {Cargo.CARGO_MAX_WEIGHT_IN_KG}kg. The specified weight is {weight_in_kg}kg.")

        if length_in_m <= 0 or width_in_m <= 0 or height_in_m <= 0:
            raise ValueError(f"Dimensions of cargo item {name} must be greater than 0. The specified dimensions are {length_in_m}m x {width_in_m}m x {height_in_m}m.")

        cargo_volume_in_m3 = length_in_m * width_in_m * height_in_m
        if cargo_volume_in_m3 > Cargo.CARGO_MAX_VOLUME_IN_M3:
            raise ValueError(f"Volume of cargo item {name} exceeds the maximum volume of {Cargo.CARGO_MAX_VOLUME_IN_M3}m3. The specified volume is {cargo_volume_in_m3}m3.")

        self.name = name
        self.weight_in_kg = weight_in_kg
        self.length_in_m = length_in_m
        self.width_in_m = width_in_m
        self.height_in_m = height_in_m

    def __str__(self):
        return f"{self.name} {self.weight_in_kg} {self.length_in_m} {self.width_in_m} {self.height_in_m}"

    def __repr__(self):
        return f"{self.name} {self.weight_in_kg} {self.length_in_m} {self.width_in_m} {self.height_in_m}"

    @staticmethod
    def from_string(cargo_str: str) -> 'Cargo':
        name, weight, length, width, height = cargo_str.split(" ")
        return Cargo(name, float(weight), float(length), float(width), float(height))

    @staticmethod
    def from_file(cargo_file: str) -> List['Cargo']:
        #
        # Reads the cargo items from a YAML file. The file is expect to be layed out as follows:
        #
        # ```yaml
        # Item1:
        #   mass: 100
        #   volume: [1, 1, 1]
        # Item2:
        #   mass: 200
        #   volume: [2, 2, 2]
        # ```

        relative = Path(cargo_file)
        if not relative.exists():
            raise ValueError(f"The file {cargo_file} does not exist. The expanded path is {relative.absolute()}.")

        result: List[Cargo] = []
        with open(relative.absolute()) as f:
            data = yaml.load(f, Loader=SafeLoader)

            for name, cargo_item_information in data.items():
                weight = cargo_item_information["mass"]
                volume_list = cargo_item_information["volume"]

                cargo_item = Cargo(str(name), weight, volume_list[0], volume_list[1], volume_list[2])
                result.append(cargo_item)

        return result

    @staticmethod
    def from_files(cargo_files: List[str]) -> List['Cargo']:
        result: List[Cargo] = []
        for file in cargo_files:
            result.extend(Cargo.from_file(file))

        return result
