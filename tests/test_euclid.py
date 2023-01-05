import pytest
from expects import equal, expect
from src.euclid import Euclid


class TestEuclid:
    @pytest.mark.parametrize(
        "first_number,second_number,result",
        [
            (10, 15, 5),
            (35, 10, 5),
            (31, 2, 1),
        ],
    )
    def test_find_gcd(self, first_number: int, second_number: int, result: int) -> None:
        euclid = Euclid()
        gcd = euclid.solve(first_number, second_number)

        expect(gcd).to(equal(result))
