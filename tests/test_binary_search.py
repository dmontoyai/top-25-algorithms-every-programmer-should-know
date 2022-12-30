import math

from expects import equal, expect

from src.binary_search import BinarySearch


class TestBinarySearch:

    def test_search_the_first_element_in_the_list(self) -> None:
        stack = list(range(16))

        steps = BinarySearch.solve(stack, 0)

        expected_steps = int(math.sqrt(len(stack)))
        expect(steps).to(equal(expected_steps))

    def test_search_the_middle_element_in_the_list_best_scenario(self) -> None:
        stack = list(range(16))

        steps = BinarySearch.solve(stack, 7)

        expect(steps).to(equal(1))

    def test_search_the_last_element_in_the_list_worst_scenario(self) -> None:
        stack = list(range(16))

        steps = BinarySearch.solve(stack, 15)

        expect(steps).to(equal(16))
