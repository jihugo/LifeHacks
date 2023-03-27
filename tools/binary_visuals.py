"""Visuals for binary operations"""
# pylint:disable=invalid-name
import math
import re


def float_to_bin(fp: float, mode: str = "simple") -> str:
    """Convert floating point to 32-bit binary with IEEE-754 standard

    Parameters
    ----------
    fp : float
    mode : str, default = simple
        "simple" returns just the binary string. "tuple" returns (S, E, M),
        "full" returns explanation
    """

    sign_int = int(fp < 0)

    if fp == 0.0:
        exponent_str = 8 * "0"
        mantissa_str = 23 * "0"
    else:
        exponent_int = int(math.log2(abs(fp)))
        exponent_str = re.split("b", bin(exponent_int + 127))[1]
        exponent_str = (8 - len(exponent_str)) * "0" + exponent_str

        mantissa_float = fp / (-1) ** sign_int / 2**exponent_int - 1

        mantissa_str = ""
        for digit_idx in range(23):
            bit = int(mantissa_float // (1 / 2 ** (digit_idx + 1)))
            mantissa_str += str(bit)
            mantissa_float -= bit * (1 / 2 ** (digit_idx + 1))

    if mode == "simple":
        return f"{sign_int}{exponent_str}{mantissa_str}"


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
