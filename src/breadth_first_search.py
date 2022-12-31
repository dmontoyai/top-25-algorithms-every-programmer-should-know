from collections import deque
from typing import Deque, TypeVar, Generic

T = TypeVar('T', str, int)


# Breadth–first search (BFS) is an algorithm for traversing or
# searching tree or graph data structures.
#
# It starts at the tree root (or some arbitrary node of a graph,
# sometimes referred to as a ‘search key’) and explores the
# neighbor nodes first before moving to the next-level neighbors.
#
# Complexity: O(|V|+|E|) where V is a number of vertices in the graph
# and E is a number of edges in the graph.
class BreadthFirstSearch(Generic[T]):

    @staticmethod
    def solve(tree: dict[T, list[T]], root: T, target: T) -> int:
        queue: Deque[T] = deque()
        queue.append(root)
        visited = set()
        steps = 0
        while queue:
            print(queue)
            steps += 1
            current = queue.popleft()
            if current == target:
                return steps
            visited.add(current)
            children = tree.get(current)
            if children:
                queue.extend(
                    [child for child in children if child not in visited])
        return steps
