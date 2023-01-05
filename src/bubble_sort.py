from typing import Generic, TypeVar

T = TypeVar("T", str, int)


# BubbleSort is an in-place comparison sorting algorithm.
#
# It repeatedly steps through the input list element by element,
# comparing the current element with the one after it,
# swapping their values if needed.
#
# Complexity: O(n^2).
class BubbleSort(Generic[T]):
    def solve(self, items: list[T]) -> list[T]:
        size = len(items)
        swapped = False
        for idx in range(size - 1):
            for idy in range(0, size - idx - 1):
                if items[idy] > items[idy + 1]:
                    swapped = True
                    items[idy], items[idy + 1] = items[idy + 1], items[idy]
            if not swapped:
                return items
        return items
