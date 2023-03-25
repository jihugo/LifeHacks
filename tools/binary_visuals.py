"""Visuals for binary operations"""
# pylint:disable=invalid-name
import re


def add(a: int | float, b: int | float) -> str:
    """Add

    Parameters
    ----------
    a, b

    Returns
    add : str
    """
    if isinstance(a, int) and isinstance(b, int):
        return _int_add(a, b)


def _int_add(a: int, b: int) -> str:
    summary = f"{a} + {b}:"

    aye = " ".join(re.split("b", bin(a))[1])
    bee = " ".join(re.split("b", bin(b))[1])
    sahm = " ".join(re.split("b", bin(a + b))[1])
    width = max(len(aye), len(bee), len(sahm)) + 4

    return (
        f"{summary}\n"
        f"\t{(width-len(aye)) * ' '}{aye}\n"
        f"\t +  {(width-len(bee)-4) * ' '}{bee}\n"
        f"\t{width*'-'}\n"
        f"\t{(width-len(sahm)) * ' '}{sahm}\n"
        f" = {a+b}"
    )
