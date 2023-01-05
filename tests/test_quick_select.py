from expects import equal, expect

from src.quick_select import QuickSelect


class TestQuickSelect:
    def test_sort_an_array_and_find_the_k_smallest_element(self) -> None:
        array = [10, 5, 1, 3]
        quick_select = QuickSelect()

        index = quick_select.solve(array, 2)  # type: ignore

        expect(index).to(equal(5))

    def test_sort_an_array_of_letters_and_find_the_k_smallest_element(self) -> None:
        array = ["z", "h", "a", "f", "x"]
        quick_select = QuickSelect()

        index = quick_select.solve(array, 0)

        expect(index).to(equal("a"))
