import collections.abc
from typing import *

import setdoc

from serialized.core.BaseSeries import BaseSeries

__all__ = ["FrozenSeries"]
Value = TypeVar("Value")


class FrozenSeries(BaseSeries[Value], collections.abc.Hashable):
    __slots__ = ()

    @setdoc.basic
    def __hash__(self: Self) -> int:
        return hash(tuple(self._data.items()))
