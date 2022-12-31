from expects import equal, expect

from src.merge_sort import MergeSort


class TestMergeSort:

    def test_sort_an_array(self) -> None:
        array = [10, 5, 1, 3]
        merge_sort = MergeSort()

        sorted_array = merge_sort.solve(array)  # type: ignore

        expect(sorted_array).to(equal([1, 3, 5, 10]))

    def test_sort_an_array_of_letters(self) -> None:
        array = ["z", "h", "a", "f", "x"]
        merge_sort = MergeSort()

        sorted_array = merge_sort.solve(array)

        expect(sorted_array).to(equal(["a", "f", "h", "x", "z"]))
