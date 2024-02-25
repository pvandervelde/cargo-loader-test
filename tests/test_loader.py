import os
import pytest

from cargo_loader.cargo import Cargo
from cargo_loader.loader import FirstFitLoader

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
        Cargo("Item1", 11, 0.5, 1, 2), # 11
        Cargo("Item1", 22, 0.5, 1, 2), # 33
        Cargo("Item1", 33, 0.5, 1, 2), # 66
        Cargo("Item1", 44, 0.5, 1, 2), # 110
        Cargo("Item1", 55, 0.5, 1, 2), # 165
        Cargo("Item1", 66, 0.5, 1, 2), # 231
        Cargo("Item1", 77, 0.5, 1, 2), # 308
        Cargo("Item1", 88, 0.5, 1, 2), # 396
        Cargo("Item1", 99, 0.5, 1, 2), # 495
        Cargo("Item1", 110, 0.5, 1, 2), # 605
        Cargo("Item1", 121, 0.5, 1, 2), # 726
        Cargo("Item1", 132, 0.5, 1, 2), # 858
        Cargo("Item1", 143, 0.5, 1, 2), # 1001
        Cargo("Item1", 154, 0.5, 1, 2), # 1155
        Cargo("Item1", 165, 0.5, 1, 2), # 1320
        Cargo("Item1", 176, 0.5, 1, 2), # 1496
        Cargo("Item1", 187, 0.5, 1, 2), # 1683
        Cargo("Item1", 188, 0.5, 1, 2), # 1871

        Cargo("Item1", 189, 0.5, 1, 2), # 189
        Cargo("Item1", 190, 0.5, 1, 2), # 379
        Cargo("Item1", 191, 0.5, 1, 2), # 570
        Cargo("Item1", 192, 0.5, 1, 2), # 762
        Cargo("Item1", 193, 0.5, 1, 2), # 955
        Cargo("Item1", 194, 0.5, 1, 2), # 1149
        Cargo("Item1", 195, 0.5, 1, 2), # 1344
        Cargo("Item1", 196, 0.5, 1, 2), # 1540
        Cargo("Item1", 197, 0.5, 1, 2), # 1737
        Cargo("Item1", 198, 0.5, 1, 2), # 1935

        Cargo("Item1", 199, 0.5, 1, 2), # 2134
    ]
    loader = FirstFitLoader()
    assert loader.load(cargo_items) == 3
