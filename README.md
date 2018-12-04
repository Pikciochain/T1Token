# Pikcio - T1Token

This project includes **Pikcio** toolkit to quickly write Pikcio compliant 
Tokens.

## Content

This project contains a toolkit package, along with token examples and unit 
tests.

It also defines what the T1 protocol requires from tokens to be compliant.

### T1 Token protocol
Any token has to offer following functions with the same signatures to be compliant.
Public attributes (not preceded by an underscore) are highly recommended but
not mandatory.

the special `_TOKEN_VERSION` attribute is mandatory.

While creating your own token, you can copy the functions that fit your case.
If any function is not entirely satisfactory, you can rewrite it completely, as
long as the signature is identical.

If some methods are part of the protocol but do not apply in your case, please
make them raise a `NotImplementedError`.

#### Recommendations
You can use the toolkit provided in this package in order to implement standard
methods.

When something goes wrong during the execution of an endpoint, it is better to
raise an appropriate exception with details rather than returning `False` or `0`.
This is not mandatory though.

#### Mandatory attributes
```python
_TOKEN_VERSION = "T1.0"
```

#### Recommended attributes
```python
name = ''
"""The friendly name of the token"""
symbol = ''
"""The symbol of the token currency. Should be 3 or 4 characters long."""
_decimals = 0  # Your number here
"""Maximum number of decimals to express any amount of that token."""
total_supply = 0
"""The current amount of the token on the market, in case some has been minted 
or burnt."""
balance_of = {}
# type: dict
"""Maps customers addresses to their current balance."""
allowances = {}
# type: dict
"""Gives for each customer a map to the amount delegates are allowed to spend 
on their behalf."""
```

#### Required functions
```python

# Initializer

def init(supply: int, name_: str, symbol_: str):
    """Initialise this token with a new name, symbol and supply."""


# Properties

def get_name() -> str:
    """Gets token name."""


def get_symbol() -> str:
    """Gets token symbol."""


def get_decimals() -> int:
    """Gets the number of decimals of the token."""


def get_total_supply() -> int:
    """Returns the current total supply for the token"""


def get_balance(address: str) -> int:
    """Gives the current balance of the specified account."""


def get_allowance(allowed_address: str, on_address: str) -> int:
    """Gives the current allowance of allowed_address on on_address account."""


# Actions

def transfer(to_address: str, amount: int) -> bool:
    """Execute a transfer from the sender to the specified address.
    
    :returns: True if execution was successful.
    """


def mint(amount: int) -> int:
    """Request tokens creation and add created amount to sender balance.
    
    :returns: new total supply.
    """


def burn(amount: int) -> int:
    """Destroy tokens. Tokens are withdrawn from sender's account.
    
    :returns: new total supply.
    """


def approve(to_address: str, amount: int) -> bool:
    """Allow specified address to spend/use some tokens from sender account.

    The approval is set to specified amount.
    
    :returns: True if execution was successful.
    """


def update_approve(to_address: str, delta_amount: int) -> int:
    """Updates the amount specified address is allowed to spend/use from
    sender account.

    The approval is incremented of the specified amount. Negative amounts
    decrease the approval.
    
    :returns: The new approval after applying delta.
    """


def transfer_from(from_address: str, to_address: str, amount: int) -> bool:
    """Executes a transfer on behalf of another address to specified recipient.

    Operation is only allowed if sender has sufficient allowance on the source
    account.
    
    :returns: True if execution was successful.
    """

```


### The Toolkit

The `pikciotok` package contains 3 main modules:
- `base`: Contains core classes and functions related to standard token 
components (balance, allowance, transfers...).
- `events`: Provides a way to register and fire events that can be propagated 
outside the execution context.
- `context`: Loaded at runtime with environment variables, such as the address 
of the endpoint invoker.

### The Examples
The *examples* folder provides a minimal token compliant with the T1 protocol

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
