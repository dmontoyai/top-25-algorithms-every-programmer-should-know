from typing import TypeVar, Generic

T = TypeVar('T', str, int)


# Quicksort is a divide-and-conquer algorithm.
#
# It works by selecting a 'pivot' element from the array
# and partitioning the other elements into two sub-arrays,
# according to whether they are less than or greater than the pivot.
#
# Complexity: O(n^2).
class QuickSort(Generic[T]):

    def solve(self, array: list[T] = []) -> list[T]:
        if len(array) <= 1:
            return array
        pivot = array[0]
        left: list[T] = []
        right: list[T] = []
        for idx in range(1, len(array)):
            item = array[idx]
            if item < pivot:
                left.append(item)
                continue
            if item >= pivot:
                right.append(item)
                continue
        return [*self.solve(left), pivot, *self.solve(right)]
