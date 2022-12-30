import math


# Given a sorted array of N integers and a target value,
# determine if the target exists in the array in logarithmic
# time using the binary search algorithm.
#
# If target exists in the array, print the index of it.
#
# Complexity:	O(log N) -> log2(N)
class BinarySearch:

    @staticmethod
    def solve(stack: list, target: int) -> int:
        steps = 0
        left = 0
        right = len(stack) - 1
        while left <= right:
            steps += 1
            middle = math.floor((left + right) / 2)
            if stack[middle] == target:
                return steps
            if stack[middle] > target:
                right = middle - 1
            if stack[middle] < target:
                left = middle + 1
        return steps
