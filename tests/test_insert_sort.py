from expects import equal, expect

from src.insert_sort import InsertSort


class TestInsertSort:
    def test_sort_an_array(self) -> None:
        array = [10, 5, 1, 3]
        insert_sort = InsertSort()

        sorted_array = insert_sort.solve(array)  # type: ignore

        expect(sorted_array).to(equal([1, 3, 5, 10]))

    def test_sort_an_array_of_letters(self) -> None:
        array = ["z", "h", "a", "f", "x"]
        insert_sort = InsertSort()

        sorted_array = insert_sort.solve(array)

        expect(sorted_array).to(equal(["a", "f", "h", "x", "z"]))
