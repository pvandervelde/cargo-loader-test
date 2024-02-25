# cargo-loader-test

A small application for calculating the number of trolley loads required to move a given amount of
cargo. The application allows you to specify the cargo items you want to load and then calculates
the number of trolley loads required to move the cargo.

This is essentially a [bin packing problem](https://en.wikipedia.org/wiki/Bin_packing_problem). The
application has implemented a few simple algorithms to solve the problem. The first algorithm is a
simple greedy algorithm that tries to fit the cargo items into the trolley in the order they are
provided. The second algorithm is a [first-fit-decreasing](https://en.wikipedia.org/wiki/First-fit-decreasing_bin_packing)
algorithm that sorts the cargo items by mass and then tries to fit them into the trolley in that
order.

## Requirements

* An item of cargo has a weight (in kg), and dimensions of length (m), width (m) and height (m).
* The maximum weight for a single item of cargo is 200kg.
* The maximum volume for a single item of cargo is 2m^3.
* A cargo trolley can carry a maximum of 2000kg with no restrictions on the volume carried.

## Create the environment

To create the environment in which this code can be run you can use conda and provide it with
the `conda.yaml` file.

```bash

conda create -n cargo-loader-test --file conda.yaml`

```

Once the environment is created you can use it by activating it with the following command:

```bash

conda activate cargo-loader-test

```

## Usage

You can run the application in two different modes. In the first mode you specify the cargo items
you want to load by using the `--cargo` argument. You can provide this argument as many times as you
want. The `cargo` takes 5 arguments as a comma separated string:

* The cargo id
* The mass of the cargo
* The length of the cargo
* The width of the cargo
* The height of the cargo

```bash

conda activate cargo-loader-test

cd <path-to-repo>

python main.py --cargo 10223,193.0,0.2,1.2,2.3 --cargo 10224,9.2,0,0,0

```

Note that the mass of a cargo item is in kg and should be between 0 and 200, zero exclusive and 200
inclusive.  And the dimensions are in meters and should be larger than 0. The encompassing volume
should be no larger than 2.0 m^3.

In the second mode you can specify a YAML file containing the cargo items you want to load. The file
should contain a list of cargo items. For example:

```yaml
10223:
    mass: 193.0
    volume: [0.2, 1.2, 2.3]
10224:
   mass: 9.2
   volume: [0.1, 0.1, 0.1]
```

```bash

conda activate cargo-loader-test

cd <path-to-repo>

python main.py --file cargo.yaml

```

For both modes you can specify the `--algorithm` argument to specify the algorithm you want to use to
load the cargo. The options are `first_fit` and `first_fit_decreasing`. If you don't specify the
algorithm the application will use the `first_fit` algorithm by default.

```bash

conda activate cargo-loader-test

cd <path-to-repo>

python main.py --file cargo.yaml --algorithm first_fit_decreasing

```

If you want to see the help for the arguments you can use the following command:

```bash

python main.py --help


```

## Testing

There are a number of [pytest](https://docs.pytest.org/en/stable/) tests that can be run to test the
functionality of the application. You can run the tests with the following command:

```bash
cd <path-to-repo>

pytest

```
