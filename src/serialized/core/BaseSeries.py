import collections.abc
from abc import abstractmethod
from itertools import repeat, starmap
from typing import *

import setdoc
from datarepr import datarepr
from iterflat import iterflat

from serialized._utils import getitem

__all__ = ["BaseSeries"]

Value = TypeVar("Value")


class BaseSeries(collections.abc.Mapping[str, Value]):
    __slots__ = ("_data",)

    @setdoc.basic
    def __contains__(self: Self, other: Any) -> bool:
        item: tuple[str, Any]
        try:
            item = getitem(*other)
        except Exception:
            return False
        return item in self.items()

    @setdoc.basic
    def __eq__(self: Self, other: Any) -> Optional[int]:
        if type(self) is not type(other):
            return False
        if self._data != other._data:
            return False
        return True

    __format__ = object.__format__

    @setdoc.basic
    def __getitem__(self: Self, key: Any) -> Any:
        return self._data[str(key)]

    @abstractmethod
    @setdoc.basic
    def __hash__(self: Self) -> int: ...

    @setdoc.basic
    def __init__(self: Self, data: Any = (), /, **kwargs: Any) -> None:
        self._data = dict(starmap(getitem, iterflat((data, kwargs.items()))))

    @setdoc.basic
    def __iter__(self: Self) -> Iterable[tuple[str, Value]]:
        yield from self._data.items()

    @setdoc.basic
    def __len__(self: Self) -> int:
        return len(self._data)

    @setdoc.basic
    def __or__(self: Self, other: Any) -> Self:
        return type(self)(iterflat((self._data.items(), other)))

    @setdoc.basic
    def __repr__(self: Self) -> str:
        return datarepr(type(self).__name__, self._data)

    @setdoc.basic
    def __reversed__(self: Self) -> Iterable:
        yield from reversed(self._data.items())

    __str__ = object.__str__

    @classmethod
    def fromkeys(cls: type[Self], keys: Iterable, value: Value = None, /):
        return cls(zip(map(str, keys), repeat(value)))

    def get(self: Self, key: Any, default: Any = None, /) -> Value:
        return self._data.get(str(key), default)

    def keys(self: Self) -> Iterable[str]:
        yield from self._data.keys()

    def items(self: Self) -> Iterable[tuple[str, Value]]:
        yield from self._data.items()

    def values(self: Self) -> Iterable[Value]:
        yield from self._data.values()
