from expects import equal, expect

from src.depth_first_search import DepthFirstSearch


class TestDepthFirstSearch:

    def test_worst_scenario(self) -> None:
        tree = {1: [2, 3], 2: [4, 5], 3: [6, 7]}
        root = list(tree.keys())[0]
        dfs = DepthFirstSearch(tree, root, 7)

        path = dfs.solve()

        expect(path).to(equal(7))

    def test_best_scenario(self) -> None:
        tree = {"a": ["b", "c"], "b": ["d", "e"], "c": ["f", "g"]}
        root = list(tree.keys())[0]
        dfs = DepthFirstSearch(tree, root, "a")

        path = dfs.solve()

        expect(path).to(equal(1))

    def test_search_in_the_middle_of_the_tree(self) -> None:
        tree = {"a": ["b", "c"], "b": ["d", "e"], "c": ["f", "g"]}
        root = list(tree.keys())[0]
        dfs = DepthFirstSearch(tree, root, "e")

        path = dfs.solve()

        expect(path).to(equal(4))
