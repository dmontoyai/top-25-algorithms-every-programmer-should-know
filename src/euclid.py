# Euclid It's an efficient method for finding the 
# GCD(Greatest  Common Divisor) of two integers.
#
# Complexity: O(log(min(a, b)).
class Euclid:
    def solve(self, a: int, b:int) -> int:
        if a == 0:
            return b 
        return self.solve(b % a, a)
