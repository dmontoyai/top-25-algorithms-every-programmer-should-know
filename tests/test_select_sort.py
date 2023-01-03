from expects import equal, expect

from src.select_sort import SelectSort


class TestSelectSort:

    def test_sort_an_array(self) -> None:
        array = [10, 5, 1, 3]
        select_sort = SelectSort()

        sorted_array = select_sort.solve(array)  # type: ignore

        expect(sorted_array).to(equal([1, 3, 5, 10]))

    def test_sort_an_array_of_letters(self) -> None:
        array = ["z", "h", "a", "f", "x"]
        select_sort = SelectSort()

        sorted_array = select_sort.solve(array)

        expect(sorted_array).to(equal(["a", "f", "h", "x", "z"]))
