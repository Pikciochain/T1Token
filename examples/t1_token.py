"""This token contains the basic required features of a T1 token.

Any token has to offer functions with the same signature to be compliant.
Public attributes (not preceded by an underscore) are highly recommended but
not mandatory.

the special _TOKEN_VERSION attribute is mandatory.

While creating your own token, you can copy the functions that fit your case.
If any function is not entirely satisfactory, you can rewrite it completely, as
long as the signature is identical.

If some methods are part of the protocol but do not apply in your case, please
make them raise a NotImplementedError.

Default behaviour can be overridden using base module global attributes.
For example, if you don't want to raise the default events like "transferred",
you can use:

base.cancel_default_events = True
"""

from pikciotok import base, context

_TOKEN_VERSION = "T1.0"

name = ''
"""The friendly name of the token"""
symbol = ''
"""The symbol of the token currency. Should be 3 or 4 characters long."""
_decimals = base.MAX_TOKEN_DECIMALS
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


# Initializer

def init(supply: int, name_: str, symbol_: str):
    """Initialise this token with a new name, symbol and supply."""
    global total_supply, name, symbol

    name, symbol = name_, symbol_
    balance_of[context.sender] = total_supply = (supply * 10 ** _decimals)


# Properties

def get_name() -> str:
    """Gets token name."""
    return name


def get_symbol() -> str:
    """Gets token symbol."""
    return symbol


def get_decimals() -> int:
    """Gets the number of decimals of the token."""
    return _decimals


def get_total_supply() -> int:
    """Returns the current total supply for the token"""
    return total_supply


def get_balance(address: str) -> int:
    """Gives the current balance of the specified account."""
    return base.Balances(balance_of).get(address)


def get_allowance(allowed_address: str, on_address: str) -> int:
    """Gives the current allowance of allowed_address on on_address account."""
    return base.Allowances(allowances).get_one(on_address, allowed_address)


# Actions

def transfer(to_address: str, amount: int) -> bool:
    """Execute a transfer from the sender to the specified address."""
    return base.transfer(balance_of, context.sender, to_address, amount)


def mint(amount: int) -> int:
    """Request tokens creation and add created amount to sender balance.
    Returns new total supply.
    """
    global total_supply
    total_supply = base.mint(balance_of, total_supply, context.sender, amount)
    return total_supply


def burn(amount: int) -> int:
    """Destroy tokens. Tokens are withdrawn from sender's account.
    Returns new total supply.
    """
    global total_supply
    total_supply = base.burn(balance_of, total_supply, context.sender, amount)
    return total_supply


def approve(to_address: str, amount: int) -> bool:
    """Allow specified address to spend/use some tokens from sender account.

    The approval is set to specified amount.
    """
    return base.approve(allowances, context.sender, to_address, amount)


def update_approve(to_address: str, delta_amount: int) -> int:
    """Updates the amount specified address is allowed to spend/use from
    sender account.

    The approval is incremented of the specified amount. Negative amounts
    decrease the approval.
    """
    return base.update_approve(allowances, context.sender, to_address,
                               delta_amount)


def transfer_from(from_address: str, to_address: str, amount: int) -> bool:
    """Executes a transfer on behalf of another address to specified recipient.

    Operation is only allowed if sender has sufficient allowance on the source
    account.
    """
    return base.transfer_from(balance_of, allowances, context.sender,
                              from_address, to_address, amount)
