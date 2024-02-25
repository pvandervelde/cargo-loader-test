import os
import pytest
from typing import Callable, Mapping, List, Tuple

from cargo_loader.cargo import Cargo

def test_should_create_valid_cargo_item_when_suppling_values():
    item = Cargo("Item", 100, 0.5, 1, 2)
    assert item.name == "Item"
    assert item.weight_in_kg == 100
    assert item.length_in_m == 0.5
    assert item.width_in_m == 1
    assert item.height_in_m == 2

def test_should_throw_exception_when_creating_item_with_too_much_weight():
    with pytest.raises(ValueError):
        Cargo("Item", 300, 1, 1, 1)

def test_should_throw_exception_when_creating_item_with_too_much_volume():
    with pytest.raises(ValueError):
        Cargo("Item", 100, 10, 10, 10)

def test_should_create_string_when_translating_item_to_string():
    cargo = Cargo("Item", 100, 0.5, 1, 2)
    assert str(cargo) == "Item 100 0.5 1 2"

def test_should_create_valid_item_when_reading_from_string():
    cargo_str = "Item 100 0.5 1 2"
    cargo = Cargo.from_string(cargo_str)
    assert cargo.name == "Item"
    assert cargo.weight_in_kg == 100
    assert cargo.length_in_m == 0.5
    assert cargo.width_in_m == 1
    assert cargo.height_in_m == 2

def test_should_create_valid_item_when_reading_from_yaml_file():
    cargo_file = os.path.join("tests", "valid_cargo_items_1.yaml")
    cargo_items = Cargo.from_file(cargo_file)
    assert len(cargo_items) == 2

    assert cargo_items[0].name == "10223"
    assert cargo_items[0].weight_in_kg == 200.0
    assert cargo_items[0].length_in_m == 0.5
    assert cargo_items[0].width_in_m == 1.0
    assert cargo_items[0].height_in_m == 2.0

    assert cargo_items[1].name == "10224"
    assert cargo_items[1].weight_in_kg == 10.0
    assert cargo_items[1].length_in_m == 4.0
    assert cargo_items[1].width_in_m == 1.0
    assert cargo_items[1].height_in_m == 0.5

def test_should_throw_exception_when_reading_from_non_existing_yaml_file():
    cargo_file = os.path.join("tests", "non_existing_cargo_items.yaml")
    with pytest.raises(ValueError):
        Cargo.from_file(cargo_file)

def test_should_create_valid_items_when_creating_from_multiple_yaml_files():
    cargo_files = [
        os.path.join("tests", "valid_cargo_items_1.yaml"),
        os.path.join("tests", "valid_cargo_items_2.yaml")
    ]
    cargo_items = Cargo.from_files(cargo_files)
    assert len(cargo_items) == 3

    assert cargo_items[0].name == "10223"
    assert cargo_items[0].weight_in_kg == 200.0
    assert cargo_items[0].length_in_m == 0.5
    assert cargo_items[0].width_in_m == 1.0
    assert cargo_items[0].height_in_m == 2.0

    assert cargo_items[1].name == "10224"
    assert cargo_items[1].weight_in_kg == 10.0
    assert cargo_items[1].length_in_m == 4.0
    assert cargo_items[1].width_in_m == 1.0
    assert cargo_items[1].height_in_m == 0.5

    assert cargo_items[2].name == "10225"
    assert cargo_items[2].weight_in_kg == 100.0
    assert cargo_items[2].length_in_m == 2.0
    assert cargo_items[2].width_in_m == 1.0
    assert cargo_items[2].height_in_m == 0.5
