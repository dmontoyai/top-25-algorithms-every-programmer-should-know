from expects import equal, expect
import pytest

from src.djikstra import Djikstra


class TestDijkstra:

    @pytest.fixture
    def graph(self) -> dict[str, dict[str, int]]:
        return {
            "a": {
                "e": 1,
                "b": 1,
                "g": 3
            },
            "b": {
                "a": 1,
                "c": 1
            },
            "c": {
                "b": 1,
                "d": 1
            },
            "d": {
                "c": 1,
                "e": 1
            },
            "e": {
                "d": 1,
                "a": 1
            },
            "f": {
                "g": 1,
                "h": 1
            },
            "g": {
                "a": 3,
                "f": 1
            },
            "h": {
                "f": 1
            }
        }

    @pytest.mark.parametrize("source,target,distance", [
        ("h", "a", 5),
        ("a", "h", 5),
        ("c", "f", 6),
    ])
    def test_find_shortest_path(self, graph: dict[str, dict[str,
                                                            int]], source: str,
                                target: str, distance: int) -> None:
        shortest_path = Djikstra.solve(graph, source, target)

        expect(shortest_path).to(equal(distance))
