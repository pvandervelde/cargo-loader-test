from abc import ABC, abstractmethod
from typing import List

from cargo_loader.cargo import Cargo
from cargo_loader.trolley import TROLLEY_MAXIMUM_CARGO_WEIGHT_IN_KG

# Provides different loader algorithms to load cargo items into a vehicle.


class CargoLoader(ABC):
    #
    # Define the loader as an abstract class so that we can define different loader algorithms.
    #
    # Because the loader doesn't need to store any state beyond the state kept during the 'load'
    # method this could also have been done with a function definition (i.e. having multiple
    # functions with the same signature but different implementations).
    # Because python doesn't have a good way to define function signatures using functions would
    # be less clear than using an abstract class.
    #
    # The loader is trying to 'solve' the [bin packing problem](https://en.wikipedia.org/wiki/Bin_packing_problem).

    @abstractmethod
    def load(self, cargo_items: List[Cargo]) -> int:
        #
        # Load the cargo items into one or more cargo trolleys and return the number of trolleys that were loaded.
        #

        # The problem specifications don't seem to care about the way the trolleys are loaded, only about how many
        # trolleys are used. This means that we don't need to store the contents of the trolleys and so we can just
        # return the number of trolleys that were used.

        # Return an invalid number so that it is clear that the method needs to be implemented.
        return -1

class FirstFitLoader(CargoLoader):
    #
    # A simple loader algorithm that tries to load as many items as possible into a trolley.
    #
    # The algorithm works by trying to load the items into the first trolley that can fit the item.
    # If no trolley can fit the item a new trolley is used. This algorithm is simple and fast but doesn't always produce
    # the best results.
    #

    def load(self, cargo_items: List[Cargo]) -> int:
        #
        # Load the cargo items into one or more cargo trolleys and return the number of trolleys that were loaded.
        #

        # Load the cargo items into trolleys
        current_trolley_weight = 0
        trolley_count = 1
        for cargo in cargo_items:
            # Try to load the cargo into an existing trolley
            if current_trolley_weight + cargo.weight_in_kg <= TROLLEY_MAXIMUM_CARGO_WEIGHT_IN_KG:
                current_trolley_weight += cargo.weight_in_kg
            else:
                # If the cargo couldn't be loaded into an existing trolley create a new trolley
                trolley_count += 1
                current_trolley_weight = cargo.weight_in_kg

        return trolley_count

class FirstFitDecreasingLoader(CargoLoader):
    #
    # A slightly clever loader algorithm that tries to load as many items as possible into a trolley.
    #
    # The algorithm works by trying to load the heaviest items first. If the item doesn't fit into the
    # current trolley a new trolley is used. This algorithm is simple and fast but doesn't always produce
    # the best results.
    #

    def load(self, cargo_items: List[Cargo]) -> int:
        #
        # Load the cargo items into one or more cargo trolleys and return the number of trolleys that were loaded.
        #

        # Sort the cargo items by weight in descending order
        cargo_items.sort(key=lambda x: x.weight_in_kg, reverse=True)

        # Load the cargo items into trolleys
        trolleys: List[int] = []
        for cargo in cargo_items:
            # Try to load the cargo into an existing trolley
            for index, current_trolley_weight in enumerate(trolleys):
                if current_trolley_weight + cargo.weight_in_kg <= TROLLEY_MAXIMUM_CARGO_WEIGHT_IN_KG:
                    trolleys[index] = current_trolley_weight + cargo.weight_in_kg
                    break
            else:
                # If the cargo couldn't be loaded into an existing trolley create a new trolley
                trolleys.append(cargo.weight_in_kg)

        return len(trolleys)
