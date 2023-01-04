# Euclid It's an efficient method for finding the
# GCD(Greatest  Common Divisor) of two integers.
#
# Complexity: O(log(min(a, b)).
class Euclid:

    def solve(self, first_number: int, second_number: int) -> int:
        if first_number == 0:
            return second_number
        return self.solve(second_number % first_number, first_number)
