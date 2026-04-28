import collections.abc
from typing import *

import setdoc
from copyable import Copyable

from serialized.core.BaseSeries import BaseSeries

__all__ = ["Series"]

MISSING = object()
Value = TypeVar("Value")


class Series(BaseSeries[Value], Copyable, collections.abc.MutableMapping[Value]):
    __slots__ = ()

    @setdoc.basic
    def __delitem__(self: Self, key: Any) -> None:
        del self._data[str(key)]

    __hash__ = None

    @setdoc.basic
    def __ior__(self: Self, other: Iterable) -> Self:
        x: Any
        y: Any
        for x, y in other:
            self._data[str(x)] = y
        return self

    @setdoc.basic
    def __setitem__(self: Self, key: Any, value: Any) -> Any:
        self._data[str(key)] = value

    def clear(self: Self) -> None:
        "This method discards all key-value-pairs."
        self._data.clear()

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self)

    @overload
    def pop(self: Self, key: Any, /) -> Value: ...

    @overload
    def pop(self: Self, key: Any, default: Any, /) -> Value: ...

    def pop(self: Self, key: Any, default: Any = MISSING, /) -> Value:
        if default is MISSING:
            return self._data.pop(str(key))
        else:
            return self._data.pop(str(key), default)

    def popitem(self: Self) -> tuple[str, Value]:
        "This method deletes and returns the last key-value-pair."
        return self._data.popitem()

    def update(self: Self, data: Iterable, /, **kwargs: Any) -> None:
        "This method updates the key-value-pairs."
        i: Iterable
        x: Any
        y: Any
        for i in (data, kwargs.items()):
            for x, y in i:
                self._data[str(x)] = y
