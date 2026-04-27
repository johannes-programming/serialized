import unittest
from typing import *

from serialized.core.FrozenSeries import FrozenSeries
from serialized.core.Series import Series

__all__ = ["Test0"]


class Test0(unittest.TestCase):
    def test_constructors(self: Self) -> None:
        FrozenSeries()
        Series()


if __name__ == "__main__":
    unittest.main()
