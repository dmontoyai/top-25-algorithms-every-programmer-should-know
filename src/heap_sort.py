from typing import Generic, TypeVar

T = TypeVar("T", str, int)


# HeapSort is an in-place comparison sorting algorithm.
#
# It divides its input into a sorted and an unsorted region,
# and it iteratively shrinks the unsorted region by extracting
# the largest element from it and inserting it into the sorted region.
#
# Complexity: O(n * log(n)).
class HeapSort(Generic[T]):
    def solve(self, items: list[T]) -> list[T]:
        size = len(items)
        index = (size - 2) // 2

        while index >= 0:
            self._heap(items, index, size)
            index -= 1

        while size:
            items[size - 1] = self._pop(items, size)
            size -= 1
        return items

    def _heap(self, items: list[T], index: int, size: int) -> None:
        left = self._left(index)
        right = self._right(index)
        largest = index
        if left < size and items[left] > items[index]:
            largest = left
        if right < size and items[right] > items[largest]:
            largest = right
        if largest != index:
            self._swap(items, index, largest)
            self._heap(items, largest, size)

    def _pop(self, items: list[T], size: int) -> T:
        top = items[0]
        items[0] = items[size - 1]
        self._heap(items, 0, size - 1)
        return top

    @staticmethod
    def _left(index: int) -> int:
        return 2 * index + 1

    @staticmethod
    def _right(index: int) -> int:
        return 2 * index + 2

    @staticmethod
    def _swap(items: list[T], idx: int, idy: int) -> None:
        temp = items[idx]
        items[idx] = items[idy]
        items[idy] = temp
