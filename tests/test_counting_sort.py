from expects import equal, expect

from src.counting_sort import CountingSort


class TestCountingSort:

    def test_sort_an_array(self) -> None:
        array = [10, 5, 1, 3]
        select_sort = CountingSort()

        sorted_array = select_sort.solve(array)  # type: ignore

        expect(sorted_array).to(equal([1, 3, 5, 10]))
