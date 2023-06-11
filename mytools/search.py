"""Search"""

import re
from typing import Iterable, Optional

from jellyfish import jaro_winkler_similarity  # pylint: disable=E0611:no-name-in-module

__all__ = ["search", "search_jaro_wink"]


def search(keyword: str, candidate: str, exclude: str | Optional[Iterable[str]] = None):
    """Determine if candidate is valid search result

    Parameters
    ----------
    keyword : str

    candidate : str

    exclude : str | Optional[Iterable[str]], default = None
    """

    if exclude is None:
        exclude = []
    elif isinstance(exclude, Iterable):
        exclude = [str(elem) for elem in exclude]
    else:
        exclude = [str(exclude)]

    if search_jaro_wink(keyword, candidate):
        for exclude_keyword in exclude:
            if search_jaro_wink(exclude_keyword, candidate):
                break
        else:
            return True
    return False


def search_jaro_wink(
    keyword: str,
    candidate: str,
    similarity_threshold: float = 0.95,
) -> bool:
    """Search using Jaro Winkler, using Jellyfish package

    Parameters
    ----------
    keyword : str

    candidate : str

    similarity_threshold : float, default = 0.95

    Returns
    -------
    search_jaro_wink : bool
        True if the keyword (or its variant) is found in candidate
    """

    keywords = re.findall(r"[\w']+|[.,!?;]", keyword)
    candidates = re.findall(r"[\w']+|[.,!?;]", candidate)  # strip punctuations

    for keyword in keywords:
        for candidate_word in candidates:
            if (
                jaro_winkler_similarity(candidate_word.lower(), keyword.lower())
                > similarity_threshold
            ):
                break
        else:
            return False
    return True
