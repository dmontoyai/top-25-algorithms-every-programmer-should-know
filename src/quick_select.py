from typing import TypeVar, Generic

T = TypeVar('T', str, int)


# QuickSelect is a selection algorithm.
#
# It is essentially the Quicksort Algorithm,
# except that one only needs to recursively
# call only one side of the partition to be re-partitioned.
#
# This changes the best case runtime from O(nlogn) to O(n).
#
# Complexity: O(n^2).
class QuickSelect(Generic[T]):

    def solve(self, items: list[T], index: int) -> T:
        return self._quick_select(items, 0, len(items) - 1, index)

    def _quick_select(self, items: list[T], lidx: int, ridx: int,
                      index: int) -> T:
        if ridx == lidx:
            return items[lidx]

        pivot_index = 0
        items[lidx], items[pivot_index] = items[pivot_index], items[lidx]
        new_ldix = lidx

        for idx in range(lidx + 1, ridx + 1):
            if items[idx] < items[lidx]:
                new_ldix += 1
                items[new_ldix], items[idx] = items[idx], items[new_ldix]

        items[new_ldix], items[lidx] = items[lidx], items[new_ldix]

        if index < new_ldix:
            return self._quick_select(items, lidx, new_ldix - 1, index)
        return self._quick_select(items, new_ldix + 1, ridx, index)
