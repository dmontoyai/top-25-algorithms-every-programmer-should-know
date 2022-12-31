from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar('T', str, int)


@dataclass
class MergeSort(Generic[T]):
    array: list[T]

    def solve(self, array: list[T] = []) -> list[T]:
        if len(array) <= 1:
            return array
        middle = int(len(array) / 2)
        left = array[:middle]
        right = array[middle:]
        return self._merge(self.solve(left), self.solve(right))

    @staticmethod
    def _merge(left: list[T], right: list[T]) -> list[T]:
        result: list[T] = []
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
                continue
            if left[0] >= right[0]:
                result.append(right.pop(0))
                continue
        return [*result, *left, *right]  # type: ignore
