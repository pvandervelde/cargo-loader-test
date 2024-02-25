# cargo-loader-test

A small application for calculating the number of trolley loads required to move a given amount of
cargo.

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
want. The `cargo` takes 5 arguments as a space separated string:

* The cargo id
* The mass of the cargo
* The length of the cargo
* The width of the cargo
* The height of the cargo

```bash

conda activate cargo-loader-test

python main.py --cargo 10223 193.0 0.2 1.2 2.3 --cargo 10224 9.2 0 0 0

```

In the second mode you can specify a YAML file containing the cargo items you want to load. The file
should contain a list of cargo items. For example:

```yaml
10223:
    mass: 193.0
    volume: [0.2, 1.2, 2.3]
10224:
   mass: 9.2
   volume: [0, 0, 0]
```

```bash

conda activate cargo-loader-test

python main.py --file cargo.yaml

```

## Testing
