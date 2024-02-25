import argparse

from typing import List, Mapping

from cargo_loader.cargo import Cargo
from cargo_loader.loader import CargoLoader, FirstFitDecreasingLoader, FirstFitLoader

# Command line argument names
ARG_FILE_LONG = "file"
ARG_CARGO_LONG = "cargo"
ARG_ALGORITHM_LONG = "algorithm"

def parse_cargo_items(arg_dict: Mapping[str, object]) -> List[Cargo]:

    cargo_items: List[Cargo] = []
    if ARG_CARGO_LONG in arg_dict and arg_dict[ARG_CARGO_LONG] is not None:
        for item in arg_dict[ARG_CARGO_LONG]:
            cargo = Cargo.from_string(item)
            cargo_items.append(cargo)

    if ARG_FILE_LONG in arg_dict and arg_dict[ARG_FILE_LONG] is not None:
        cargo_items.extend(Cargo.from_files(arg_dict[ARG_FILE_LONG]))

    return cargo_items

def read_arguments() -> Mapping[str, any]:
    # Define the command line arguments so that we can parse them
    # There are three possible arguments:
    #
    #  - -a, --algorithm: The name of the algorithm that should be used for the to sort the cargo items
    #                     into trollys. Current options are: 'first_fit', 'first_fit_decreasing'
    #  - -f, --file: The file path for the input file which contains the list of cargo items. It
    #                is expected that the file contains all the cargo items specified in YAML format.
    #                For an example see the example_cargo_small.yaml file in the samples directory.
    #  - -c, --cargo: The information of a cargo item given as a string. The format is 'name weight length width height'.
    #                 This argument can be specified multiple times.
    #
    # The --file and --cargo arguments are mutually exclusive, but at least one of them is required.
    #

    parser = argparse.ArgumentParser(
        description="Simulate a 4 wheel steering robot in 2D",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        "-a",
        f"--{ARG_ALGORITHM_LONG}",
        action="store",
        choices=['first_fit', 'first_fit_decreasing',],
        default='first_fit',
        required=False,
        help="The name of the algorithm that should be used for the to sort the cargo items into trollys. Current options are: 'first_fit', 'first_fit_decreasing'")

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
    if ARG_ALGORITHM_LONG in arg_dict and arg_dict[ARG_ALGORITHM_LONG] is not None:
        if arg_dict[ARG_ALGORITHM_LONG] == 'first_fit':
            return FirstFitLoader()
        elif arg_dict[ARG_ALGORITHM_LONG] == 'first_fit_decreasing':
            return FirstFitDecreasingLoader()

    return FirstFitLoader()

def main(args=None):
    arg_dict = read_arguments()
    cargo_items = parse_cargo_items(arg_dict)

    loader = select_loader(arg_dict)

    print(f"Loading {len(cargo_items)} items into trolleys using {loader.__class__.__name__} ...")

    count = loader.load(cargo_items)
    print(f"Loaded {len(cargo_items)} items into {count} { 'trolley' if count == 1 else 'trolleys'}")

if __name__ == '__main__':
    main()
