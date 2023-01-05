from typing import TypeVar, Generic

T = TypeVar("T", str, int)


# BoyerMoore  is an algorithm for finding the majority of a sequence.
#
# First it finds a majority element.
# Second pass verify that the element found in the first pass really is a majority.
#
# Time Complexity: O(N).
# Space Complexity: O(1).
class BoyerMoore(Generic[T]):
    @staticmethod
    def solve(items: list[T]) -> T | None:
        candidate: T | None = None
        votes = 0
        for item in items:
            if not votes:
                candidate = item
            votes += 1 if item == candidate else -1

        count = sum(1 for i in range(len(items)) if items[i] == candidate)

        if count > len(items) // 2:
            return candidate
        return None
