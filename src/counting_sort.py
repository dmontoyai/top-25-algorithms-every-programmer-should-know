from typing import TypeVar, Generic

T = TypeVar("T", str, int)


# CountingSort is an integer sorting algorithm.
#
# It operates by counting the number of objects that possess
# distinct key values, and applying prefix sum on those counts
# to determine the positions of each key value in the output sequence.
#
# Complexity: O(n+k).
class CountingSort(Generic[T]):
    MAX_RANGE = 256

    def solve(self, items: list[T]) -> list[T]:
        default_value = 0 if isinstance(items[0], int) else ""
        sorted_items = [default_value for _ in range(len(items))]
        count = [default_value for _ in range(self.MAX_RANGE)]

        for item in items:
            count[item] += 1  # type: ignore
        for index in range(self.MAX_RANGE):
            count[index] += count[index - 1]  # type: ignore
        for item in items:
            sorted_items[count[item] - 1] = item  # type: ignore
            count[item] -= 1  # type: ignore

        return sorted_items  # type: ignore
