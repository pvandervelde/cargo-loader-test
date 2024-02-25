import os
import pytest

from cargo_loader.cargo import Cargo
from cargo_loader.loader import FirstFitDecreasingLoader, FirstFitLoader

#
# FirstFitLoader
#

def test_first_fit_loader_should_load_single_item_into_single_trolley():
    cargo_items = [Cargo("Item", 100, 0.5, 1, 2)]
    loader = FirstFitLoader()
    assert loader.load(cargo_items) == 1

def test_first_fit_loader_should_load_two_items_into_single_trolley():
    cargo_items = [Cargo("Item1", 100, 0.5, 1, 2), Cargo("Item2", 100, 0.5, 1, 2)]
    loader = FirstFitLoader()
    assert loader.load(cargo_items) == 1

def test_first_fit_loader_should_load_multiple_items_into_two_trolleys():
    cargo_items = [Cargo("Item1", 100, 0.5, 1, 2) for _ in range(21)]
    loader = FirstFitLoader()
    assert loader.load(cargo_items) == 2

def test_first_fit_loader_should_load_multiple_items_into_multiple_trolleys():
    cargo_items = [
        Cargo("Item1", 10, 0.5, 1, 2),
        Cargo("Item1", 10, 0.5, 1, 2),
        Cargo("Item1", 10, 0.5, 1, 2),
        Cargo("Item1", 10, 0.5, 1, 2),
        Cargo("Item1", 10, 0.5, 1, 2),
        Cargo("Item1", 10, 0.5, 1, 2),
        Cargo("Item1", 10, 0.5, 1, 2),
        Cargo("Item1", 10, 0.5, 1, 2),
        Cargo("Item1", 10, 0.5, 1, 2),
        Cargo("Item1", 10, 0.5, 1, 2),

        Cargo("Item1", 200, 0.5, 1, 2),
        Cargo("Item1", 200, 0.5, 1, 2),
        Cargo("Item1", 200, 0.5, 1, 2),
        Cargo("Item1", 200, 0.5, 1, 2),
        Cargo("Item1", 200, 0.5, 1, 2),
        Cargo("Item1", 200, 0.5, 1, 2),
        Cargo("Item1", 200, 0.5, 1, 2),
        Cargo("Item1", 200, 0.5, 1, 2),
        Cargo("Item1", 200, 0.5, 1, 2),
        Cargo("Item1", 200, 0.5, 1, 2),

        Cargo("Item1", 190, 0.5, 1, 2),
        Cargo("Item1", 190, 0.5, 1, 2),
        Cargo("Item1", 190, 0.5, 1, 2),
        Cargo("Item1", 190, 0.5, 1, 2),
        Cargo("Item1", 190, 0.5, 1, 2),
        Cargo("Item1", 190, 0.5, 1, 2),
        Cargo("Item1", 190, 0.5, 1, 2),
        Cargo("Item1", 190, 0.5, 1, 2),
        Cargo("Item1", 190, 0.5, 1, 2),
        Cargo("Item1", 190, 0.5, 1, 2),

    ]
    loader = FirstFitLoader()
    assert loader.load(cargo_items) == 3

#
# FirstFitDecreasingLoader
#

def test_first_fit_decreasing_loader_should_load_single_item_into_single_trolley():
    cargo_items = [Cargo("Item", 100, 0.5, 1, 2)]
    loader = FirstFitDecreasingLoader()
    assert loader.load(cargo_items) == 1

def test_first_fit_decreasing_loader_should_load_two_items_into_single_trolley():
    cargo_items = [Cargo("Item1", 100, 0.5, 1, 2), Cargo("Item2", 100, 0.5, 1, 2)]
    loader = FirstFitDecreasingLoader()
    assert loader.load(cargo_items) == 1

def test_first_fit_decreasing_loader_should_load_multiple_items_into_two_trolleys():
    cargo_items = [Cargo("Item1", 100, 0.5, 1, 2) for _ in range(21)]
    loader = FirstFitDecreasingLoader()
    assert loader.load(cargo_items) == 2

def test_first_fit_decreasing_loader_should_load_multiple_items_into_multiple_trolleys():
    cargo_items = [
        Cargo("Item1", 10, 0.5, 1, 2),
        Cargo("Item1", 10, 0.5, 1, 2),
        Cargo("Item1", 10, 0.5, 1, 2),
        Cargo("Item1", 10, 0.5, 1, 2),
        Cargo("Item1", 10, 0.5, 1, 2),
        Cargo("Item1", 10, 0.5, 1, 2),
        Cargo("Item1", 10, 0.5, 1, 2),
        Cargo("Item1", 10, 0.5, 1, 2),
        Cargo("Item1", 10, 0.5, 1, 2),
        Cargo("Item1", 10, 0.5, 1, 2),

        Cargo("Item1", 200, 0.5, 1, 2),
        Cargo("Item1", 200, 0.5, 1, 2),
        Cargo("Item1", 200, 0.5, 1, 2),
        Cargo("Item1", 200, 0.5, 1, 2),
        Cargo("Item1", 200, 0.5, 1, 2),
        Cargo("Item1", 200, 0.5, 1, 2),
        Cargo("Item1", 200, 0.5, 1, 2),
        Cargo("Item1", 200, 0.5, 1, 2),
        Cargo("Item1", 200, 0.5, 1, 2),
        Cargo("Item1", 200, 0.5, 1, 2),

        Cargo("Item1", 190, 0.5, 1, 2),
        Cargo("Item1", 190, 0.5, 1, 2),
        Cargo("Item1", 190, 0.5, 1, 2),
        Cargo("Item1", 190, 0.5, 1, 2),
        Cargo("Item1", 190, 0.5, 1, 2),
        Cargo("Item1", 190, 0.5, 1, 2),
        Cargo("Item1", 190, 0.5, 1, 2),
        Cargo("Item1", 190, 0.5, 1, 2),
        Cargo("Item1", 190, 0.5, 1, 2),
        Cargo("Item1", 190, 0.5, 1, 2),
    ]
    loader = FirstFitDecreasingLoader()
    assert loader.load(cargo_items) == 2
