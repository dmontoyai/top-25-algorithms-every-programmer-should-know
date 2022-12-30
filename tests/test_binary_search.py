import math
import pytest

from expects import equal, expect

from src.binary_search import BinarySearch


class TestBinarySearch:

    @pytest.fixture
    def stack(self) -> list:
        return list(range(16))

    def test_search_the_first_element_in_the_list_worst_scenario(
            self, stack: list) -> None:
        steps = BinarySearch.solve(stack, 0)

        expected_steps = int(math.sqrt(len(stack)))
        expect(steps).to(equal(expected_steps))

    def test_search_the_middle_element_in_the_list_best_scenario(
            self, stack: list) -> None:
        steps = BinarySearch.solve(stack, 7)

        expect(steps).to(equal(1))

    def test_search_the_last_element_in_the_list(self, stack: list) -> None:
        steps = BinarySearch.solve(stack, 15)

        expect(steps).to(equal(5))
