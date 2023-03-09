__all__ = ["variable_rolling_mean", "circular_convolution"]

from typing import Iterable
import numpy as np
import warnings


def variable_rolling_mean(array: Iterable[float], kernel_size: int) -> np.ndarray:
    """Apply rolling average convolution with variable kernel size
    at the beginning and end, leading to no boundary effect"""
    if kernel_size > len(array):
        kernel_size = len(array)

    convolved = np.convolve(
        np.array(array, dtype=float),
        np.repeat([1 / kernel_size], kernel_size),
        mode="same",
    )

    for idx in range(int(kernel_size / 2)):
        convolved[idx] = np.mean(array[: idx + 1])
        convolved[-idx - 1] = np.mean(array[-idx - 1 :])
    return convolved


def circular_convolution(array: Iterable[float], kernel: Iterable[float]) -> np.ndarray:
    kernel_size = kernel.shape[0]

    if kernel_size % 2 == 0:
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
