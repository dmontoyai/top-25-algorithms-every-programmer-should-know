from typing import Generic, TypeVar

T = TypeVar('T', str, int)

# SelectSort is an in-place comparison sorting algorithm.
#
# The algorithm divides the input list into two parts:
# a sorted sublist of items which is built up from left to
# right at the front (left) of the list
# and a sublist of the remaining unsorted items that occupy the rest of the list.
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
