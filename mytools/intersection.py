"""Get intersection point from 2 discrete curves"""
__all__ = ["get_intersection_points", "get_one_intersection_point"]

from typing import Iterable, Tuple
import numpy as np


def get_intersection_points(
    x1: Iterable, y1: Iterable, x2: Iterable, y2: Iterable
) -> Tuple[Tuple[float, float], Tuple[float, float]]:
    """Get intersection points between 2 discrete curves"""

    def distance(xa, ya, xb, yb) -> float:
        return np.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

    min_distance = float("inf")

    for x1_point, y1_point in iter(zip(x1, y1)):
        for x2_point, y2_point in iter(zip(x2, y2)):
            curr_dist = distance(x1_point, y1_point, x2_point, y2_point)
            if curr_dist < min_distance:
                min_distance = curr_dist
                points_1 = (x1_point, y1_point)
                points_2 = (x2_point, y2_point)

    return points_1, points_2


def get_one_intersection_point(
    x1: Iterable, y1: Iterable, x2: Iterable, y2: Iterable
) -> Tuple[float, float]:
    """Get single intersection point between 2 discrete curves"""

    points_1, points_2 = get_intersection_points(x1, y1, x2, y2)
    return ((points_1[0] + points_2[0]) / 2, (points_1[1] + points_2[1]) / 2)
