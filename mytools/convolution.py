"""Some useful python fucntions"""
__all__ = ["variable_rolling_mean", "circular_convolution"]

from typing import Iterable
import warnings
import numpy as np


def variable_rolling_mean(
    array: Iterable[float], kernel_size: int, suppress_warning: bool = False
) -> np.ndarray:
    """Apply rolling average convolution with variable kernel size
    at the beginning and end, leading to no boundary effect"""
    if kernel_size == 0:
        if not suppress_warning:
            warnings.warn("Don't fool me")
        return array

    if len(array) == 0:
        if not suppress_warning:
            warnings.warn("Got empty array, returning empty array")
        return array

    if kernel_size > len(array):
        kernel_size = len(array)
        if not suppress_warning:
            warnings.warn(
                "Kernel size < array length, so kernel size is now set to array length"
            )

    convolved = np.convolve(
        np.array(array, dtype=float),
        np.repeat([1 / kernel_size], kernel_size),
        mode="same",
    )

    for idx in range(int(kernel_size / 2)):
        convolved[idx] = np.mean(array[: idx + 1])
        convolved[-idx - 1] = np.mean(array[-idx - 1 :])
    return convolved


def circular_convolution(
    array: Iterable[float], kernel: Iterable[float], suppress_warning: bool = False
) -> np.ndarray:
    """Apply convolution in a circle, where the start and end of the array is stitched
    together, resulting in no boundary effect."""
    kernel_size = len(kernel)

    if kernel_size % 2 == 0 and not suppress_warning:
        warnings.warn("Convolution kernel size is even, so result is shifted.")

    tip = np.concatenate([array[-(kernel_size - 1) :], array[: kernel_size - 1]])

    main_convolved = np.convolve(array, kernel, mode="valid")
    tip_convolved = np.convolve(tip, kernel, mode="valid")

    return np.concatenate(
        [
            tip_convolved[int(kernel_size / 2) :],
            main_convolved,
            tip_convolved[: int(kernel_size / 2)],
        ]
    )
