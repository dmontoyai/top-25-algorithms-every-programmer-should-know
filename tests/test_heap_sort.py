from expects import equal, expect

from src.heap_sort import HeapSort


class TestHeapSort:
    def test_sort_an_array(self) -> None:
        array = [10, 5, 1, 3]
        heap_sort = HeapSort()

        sorted_array = heap_sort.solve(array)  # type: ignore

        expect(sorted_array).to(equal([1, 3, 5, 10]))

    def test_sort_an_array_of_letters(self) -> None:
        array = ["z", "h", "a", "f", "x"]
        heap_sort = HeapSort()

        sorted_array = heap_sort.solve(array)

        expect(sorted_array).to(equal(["a", "f", "h", "x", "z"]))
