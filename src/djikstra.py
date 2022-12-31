# Dijkstra is an algorithm for finding the shortest
# paths between nodes in a graph.
#
# For a given source node in the graph,
# the algorithm finds the shortest path between that node
# and every other.
#
# Complexity: (|V|+|E|)log2|V| where |V| is the number of nodes
from collections import defaultdict
from dataclasses import dataclass
import math


@dataclass
class Item:
    distance: float
    neightbords: list[str]


class Djikstra:

    @staticmethod
    def solve(graph: dict[str, dict[str, int]], source: str,
              target: str) -> int:
        solutions: dict[str, Item] = defaultdict()
        solutions[source] = Item(0, [])

        while True:
            parent: list[str] = []
            nearest = ""
            distance = math.inf

            for solution in solutions.keys():
                if not solutions[solution]:
                    continue
                ndist = solutions[solution].distance
                neighbours = graph[solution]

                for neighbour in neighbours.keys():
                    if solutions.get(neighbour):
                        continue

                    new_distance = neighbours[neighbour] + ndist

                    if new_distance < distance:
                        parent = solutions[solution].neightbords
                        nearest = neighbour
                        distance = new_distance

            if distance == math.inf:
                break

            solutions[nearest] = Item(distance, [*parent, nearest])

        return int(solutions[target].distance)
