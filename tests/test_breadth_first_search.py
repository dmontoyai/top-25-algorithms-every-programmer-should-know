from expects import equal, expect

from src.breadth_first_search import BreadthFirstSearch


class TestBreadthFirstSearch:

    def test_dummy(self) -> None:
        graph = [[0, 1], [1, 2]]
        steps = BreadthFirstSearch.solve(graph, 2)
        expect(steps).to(equal(0))
