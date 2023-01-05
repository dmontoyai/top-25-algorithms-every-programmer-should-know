from typing import Generic, TypeVar

T = TypeVar("T", str, int)


# SelectSort is an in-place comparison sorting algorithm.
#
# It works sorting an array by repeatedly finding the minimum element
# and putting it at the beginning
#
# Complexity: O(n^2).
class SelectSort(Generic[T]):
    def solve(self, items: list[T]) -> list[T]:
        size = len(items)
        for idx in range(size):
            min_index = idx
            for idy in range(idx + 1, size):
                if items[idy] < items[min_index]:
                    min_index = idy
            items[idx], items[min_index] = items[min_index], items[idx]
        return items
