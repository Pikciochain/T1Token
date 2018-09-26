# Pikcio - T1Token

This project includes **Pikcio** toolkit to quickly write Pikcio compliant 
Tokens.

## Content

This project contains a toolkit package, along with token examples and unit 
tests.

### The Toolkit

The `pikciotok` package contains 3 main modules:
- `base`: Contains core classes and functions related to standard token 
components (balance, allowance, transfers...).
- `events`: Provides a way to register and fire events that can be propagated 
outside the execution context.
- `context`: Loaded at runtime with environment variables, such as the address 
of the endpoint invoker.

### The Examples
The *examples* folder provides token use cases to help you get started and build 
your own token contract.

## Getting Started

These instructions will get you a copy of the project up and running on your 
local machine for development and testing purposes. 
See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This project is built upon **Python 3**.
There is no other prerequisite or third-party required.


### Installing

After cloning the repository on your machine, it is encouraged to create a
virtual environment using your preferred tool. If you have no preference, you
can have a look at `virtualenvwrapper`, easily installed with:

```bash
pip install virtualenvwrapper
```

Once your environment ready and activated, install the pyton depencies using:

```bash
pip install -r requirements.txt
```

Optionally, if you also want to debug, develop or test the project, use:

```bash
pip install -r dev-requirements.txt
```

## Running the tests

Tests are run using following command at the root of the project:

```bash
pytest
```

All tests are kept under the `tests` folder at the root of the project.

## Authors

- **Jorick Lartigau** - *Development Lead* - [Pikcio](https://pikciochain.com)
- **Thibault Drevon** - *Architecture and implementation* - [Yellowstones](http://www.yellowstones.io)
