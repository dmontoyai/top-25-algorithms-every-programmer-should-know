from expects import be_none, equal, expect

from src.boyer_moore import BoyerMoore


class TestBoyerMooreSort:

    def test_find_the_mayority_number(self) -> None:
        array = [10, 5, 1, 3, 1, 10, 1, 1, 1, 1]
        boyer_moore = BoyerMoore()

        most_frequent = boyer_moore.solve(array)  # type: ignore

        expect(most_frequent).to(equal(1))

    def test_return_none_if_there_is_no_mayority(self) -> None:
        array = [1, 2, 3]
        boyer_moore = BoyerMoore()

        most_frequent = boyer_moore.solve(array)  # type: ignore

        expect(most_frequent).to(be_none)

    def test_find_the_mayority_letter(self) -> None:
        array = ["z", "h", "z"]
        boyer_moore = BoyerMoore()

        most_frequent = boyer_moore.solve(array)

        expect(most_frequent).to(equal("z"))
