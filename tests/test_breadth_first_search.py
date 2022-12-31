from expects import equal, expect

from src.breadth_first_search import BreadthFirstSearch


class TestBreadthFirstSearch:

    def test_worst_scenario(self) -> None:
        tree = {1: [2, 3], 2: [4, 5], 3: [6, 7]}
        root = list(tree.keys())[0]
        path = BreadthFirstSearch.solve(tree, root, 7)

        expect(path).to(equal(7))

    def test_best_scenario(self) -> None:
        tree = {"a": ["b", "c"], "b": ["d", "e"], "c": ["f", "g"]}
        root = list(tree.keys())[0]
        path = BreadthFirstSearch.solve(tree, root, "a")

        expect(path).to(equal(1))

    def test_search_in_the_middle_of_the_tree(self) -> None:
        tree = {"a": ["b", "c"], "b": ["d", "e"], "c": ["f", "g"]}
        root = list(tree.keys())[0]
        path = BreadthFirstSearch.solve(tree, root, "e")

        expect(path).to(equal(5))
