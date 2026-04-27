from itertools import starmap
from typing import *

__all__ = ["getitem", "getitems"]


def getitem(key: Any, value: Any) -> tuple[str, Any]:
    return str(key), value


def getitems(data: Iterable, /, **kwargs: Any) -> Iterable[tuple[str, Any]]:
    return starmap(getitem, dict(data, **kwargs).items())
