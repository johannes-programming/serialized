from itertools import starmap
from typing import *

from iterflat import iterflat

__all__ = ["getitem", "getitems"]


def getitem(key: Any, value: Any) -> tuple[str, Any]:
    return str(key), value
