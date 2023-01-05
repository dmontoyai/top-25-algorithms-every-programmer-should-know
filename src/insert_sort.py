from typing import Generic, TypeVar

T = TypeVar("T", str, int)

# InsertSort is an in-place comparison sorting algorithm.
#
# At each array-position, it checks the value there against
# the largest value in the sorted list.
#
# If larger, it leaves the element in place and moves to the next.
# If smaller, it finds the correct position within the sorted list,
# and inserts into that correct position.
#
# Complexity: O(n^2).


class InsertSort(Generic[T]):
    def solve(self, items: list[T]) -> list[T]:
        size = len(items)
        for idx in range(1, size):
            key = items[idx]
            idy = idx - 1
            while idy >= 0 and key < items[idy]:
                items[idy + 1] = items[idy]
                idy -= 1
            items[idy + 1] = key
        return items
