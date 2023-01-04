import pytest
from expects import equal, expect
from src.euclid import Euclid


class TestEuclid:

    @pytest.mark.parametrize("a,b,result", [
        (10, 15, 5),
        (35, 10, 5),
        (31, 2, 1),
    ])
    def test_find_gcd(self, a: int, b: int, result: int) -> None:
        euclid = Euclid()
        gcd = euclid.solve(a, b)

        expect(gcd).to(equal(result))
