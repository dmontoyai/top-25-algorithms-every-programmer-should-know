import math

from expects import equal, expect

from src.binary_search import BinarySearch


class TestBinarySearch:
    def test_worst_scenario(self) -> None:
        stack = [chr(97 + index) for index in range(16)]

        steps = BinarySearch.solve(stack, "a")

        expected_steps = int(math.sqrt(len(stack)))
        expect(steps).to(equal(expected_steps))

    def test_best_scenario(self) -> None:
        stack = list(range(16))

        steps = BinarySearch.solve(stack, 7)

        expect(steps).to(equal(1))

    def test_search_the_last_element_in_the_list(self) -> None:
        stack = [chr(97 + index) for index in range(16)]
        steps = BinarySearch.solve(stack, "p")
        print(stack)

        expect(steps).to(equal(5))
