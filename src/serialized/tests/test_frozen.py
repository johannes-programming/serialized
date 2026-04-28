import unittest
from typing import *

from serialized.core.FrozenSeries import FrozenSeries

__all__ = ["Test0"]


class TestFrozen(unittest.TestCase):
    def test_frozen(self: Self) -> None:
        obj: FrozenSeries
        obj = FrozenSeries([["hello", "world"], [4, 2]])
        hash(obj)
        obj = FrozenSeries([[[], "world"], [4, 2]])
        hash(obj)
        obj = FrozenSeries([["hello", []], [4, 2]])
        with self.assertRaises(Exception):
            hash(obj)


if __name__ == "__main__":
    unittest.main()
