import argparse
from os import makedirs, path
from pathlib import Path

from typing import Callable, List, Mapping, NamedTuple, Tuple

from cargo_loader.cargo import Cargo
from cargo_loader.loader import CargoLoader, FirstFitLoader

ARG_FILE_LONG = "file"
ARG_CARGO_LONG = "cargo"

def parse_cargo_items(arg_dict: Mapping[str, object]) -> List[Cargo]:
    cargo_items: List[Cargo] = []
    if ARG_CARGO_LONG in arg_dict and arg_dict[ARG_CARGO_LONG] is not None:
        for i, item in enumerate(arg_dict[ARG_CARGO_LONG]):
            cargo = Cargo.from_string(item)
            cargo_items.append(cargo)

    if ARG_FILE_LONG in arg_dict and arg_dict[ARG_FILE_LONG] is not None:
        cargo_items.extend(Cargo.from_files(arg_dict[ARG_FILE_LONG]))

    return cargo_items

def read_arguments() -> Mapping[str, any]:
    # Define the command line arguments so that we can parse them
    # There are two possible arguments:
    #
    #  - -f, --file: The file path for the input file which contains the list of cargo items. It
    #                is expected that the file contains all the cargo items specified in YAML format.
    #                For an example see the example_cargo_small.yaml file in the samples directory.
    #  - -c, --cargo: The information of a cargo item given as a string. The format is 'name weight length width height'.
    #                 This argument can be specified multiple times.
    #

    parser = argparse.ArgumentParser(
        description="Simulate a 4 wheel steering robot in 2D",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        "-f",
        f"--{ARG_FILE_LONG}",
        action="append",
        required=False,
        type=str,
        help="The file path for the input file which contains the list of cargo items.",
    )

    group.add_argument(
        "-c",
        f"--{ARG_CARGO_LONG}",
        action="append",
        required=False,
        type=str,
        help="The information of a cargo item. The format is 'name,weight,length,width,height'. Can be specified multiple times.",
    )

    args = parser.parse_args()
    return vars(args)

def select_loader(arg_dict: Mapping[str, object]) -> CargoLoader:
    # Select the loader algorithm to use
    # For now we only have the FirstFitLoader but we can add more loaders in the future.
    return FirstFitLoader()

def main(args=None):
    arg_dict = read_arguments()
    cargo_items = parse_cargo_items(arg_dict)

    loader = select_loader(arg_dict)

    count = loader.load(cargo_items)
    print(f"Loaded {len(cargo_items)} items into {count} { 'trolley' if count == 1 else 'trolleys'}")

if __name__ == '__main__':
    main()
