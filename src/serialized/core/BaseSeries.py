import collections.abc
from abc import abstractmethod
from typing import *

import cmp3
import setdoc
from datarepr import datarepr
from iterflat import iterflat

from serialized._utils import getitem, getitems

__all__ = ["BaseSeries"]

Value = TypeVar("Value")


class BaseSeries(cmp3.CmpABC, collections.abc.Mapping[str, Value]):
    __slots__ = ("_data",)

    def __cmp__(self: Self, other: Any) -> Any:
        if type(self) is not type(other):
            return
        return cmp3.cmp(self._data, other._data, mode="eq")

    def __contains__(self: Self, other: Any) -> bool:
        item: tuple[str, Any]
        try:
            item = getitem(*other)
        except Exception:
            return False
        return item in self.items()

    __format__ = object.__format__

    @setdoc.basic
    def __getitem__(self: Self, key: Any) -> Any:
        return self._data[str(key)]

    @abstractmethod
    def __hash__(self: Self) -> int: ...

    def __init__(self: Self, data: Any = (), /, **kwargs: Any) -> None:
        self._data = dict(getitems(data, **kwargs))

    def __iter__(self: Self) -> Iterable:
        return self._data.items()

    def __len__(self: Self) -> int:
        return len(self._data)

    def __or__(self: Self, other: Any) -> Self:
        return type(self)(iterflat((self._data.items(), getitems(other))))

    def __repr__(self: Self) -> str:
        return datarepr(type(self).__name__, self._data)

    def __reversed__(self: Self) -> Iterable:
        yield from reversed(self._data.items())

    __str__ = object.__str__

    @classmethod
    def fromkeys(cls: type[Self], keys: Iterable, value: Value = None, /):
        return cls(dict.fromkeys(keys, value))

    def get(self: Self, key: Any, default: Any = None, /) -> Value:
        return self._data.get(str(key), default)

    def keys(self: Self) -> Iterable[str]:
        yield from self._data.keys()

    def items(self: Self) -> Iterable[tuple[str, Value]]:
        yield from self._data.items()

    def values(self: Self) -> Iterable[Value]:
        yield from self._data.values()
