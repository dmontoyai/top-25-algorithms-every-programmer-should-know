from collections import deque
from dataclasses import dataclass
from typing import Deque, TypeVar, Generic

T = TypeVar("T", str, int)


# Depth-first search (DFS) is an algorithm for traversing or searching
# tree or graph data structures.
#
# The algorithm starts at the root node (selecting some arbitrary node
# as the root node in the case of a graph) and explores as far as
# possible along each branch before backtracking.
#
# Complexity: O(|V|+|E|) where V is a number of vertices in the graph
# and E is a number of edges in the graph.
@dataclass
class DepthFirstSearch(Generic[T]):
    tree: dict[T, list[T]]
    root: T
    target: T

    def solve(self) -> int:
        path = self._dfs(self.tree, self.root, self.target, [])
        return path.index(self.target) + 1

    def _dfs(
        self, tree: dict[T, list[T]], root: T, target: T, path: list[T]
    ) -> list[T]:
        queue: Deque[T] = deque()
        queue.append(root)
        path = []
        while queue:
            current = queue.popleft()
            if current == target:
                path.append(current)
                return path
            path.append(current)
            children = tree.get(current)
            if children:
                for child in children:
                    path.extend(self._dfs(tree, child, target, path))
        return path
