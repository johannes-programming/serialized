import collections.abc
from typing import *

import setdoc
from copyable import Copyable

from serialized._utils import getitems
from serialized.core.BaseSeries import BaseSeries

__all__ = ["Series"]

MISSING = object()
Value = TypeVar("Value")


class Series(BaseSeries[Value], Copyable, collections.abc.MutableMapping):
    __slots__ = ()

    @setdoc.basic
    def __delitem__(self: Self, key: Any) -> None:
        del self._data[str(key)]

    __hash__ = None

    @setdoc.basic
    def __ior__(self: Self, other: Any) -> Self:
        self._data |= getitems(other)
        return self

    @setdoc.basic
    def __setitem__(self: Self, key: Any, value: Any) -> Any:
        self._data[str(key)] = value

    def clear(self: Self) -> None:
        self._data.clear()

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)

    def pop(self: Self, key: Any, default: Any = MISSING, /) -> Value:
        if default is MISSING:
            return self._data.pop(str(key))
        else:
            return self._data.pop(str(key), default)

    def popitem(self: Self) -> tuple[str, Value]:
        return self._data.popitem()

    def update(self: Self, data: Any, /, **kwargs: Any) -> None:
        self._data.update(getitems(data, **kwargs))
        return self
