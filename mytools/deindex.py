"""Tools to de-index arrays"""
__all__ = ["raster_select"]

import numpy as np


def raster_select(
    length: int, center: float, width: float, normalize: str = None
) -> np.ndarray:
    """Returns an array with specified length where selection is made around center
    with specified width.

    Parameters
    ----------
    length : int
        length of entire array

    center : float
        center for selection region

    width : float
        width of selection region

    normalize : str, default = None
        None will not normalize result.

        "sum" will normalize result such that elements add up to 1.

        "vector" will normalize result such that sum of squares of element add up to 1.
    """
    start = center - width / 2
    end = center + width / 2
    if start < 0 or end > length:
        raise UserWarning("bin width too large!")

    result = np.zeros(length)
    if int(start) == int(end):
        result[int(start)] = width

    else:
        result[int(start)] = 1 - start % 1

        if end != int(end):
            result[int(end)] = end % 1

        if int(start) + 1 != int(end):
            result[int(start) + 1 : int(end)] = [
                1 for _ in range(int(end - int(start) - 1))
            ]

    if normalize == "sum":
        result /= width

    if normalize == "vector":
        result /= np.linalg.norm(result)

    return result


def raster_bin_sum(array: np.ndarray, center: float, width: float) -> float:
    """Get the sum of the bin on an array

    Parameters
    ----------
    array : NumPy 1D array

    center : float
        Center of desired bin, unit = index

    width : float
        Width of desired bin, unit = index
    """
    return np.sum(
        np.multiply(
            array,
            raster_select(
                length=len(array), center=center, width=width, normalize=None
            ),
        )
    )
