/**
 * Dijkstra is an algorithm for finding the shortest
 * paths between nodes in a graph.
 *
 * For a given source node in the graph,
 * the algorithm finds the shortest path between that node
 * and every other.
 *
 * Complexity: (|V|+|E|)log2|V| where |V| is the number of nodes
 * and |E| is the number of edges.
 */
function dijkstra(graph, source) {
  const solutions = {};
  solutions[source] = [];
  solutions[source].dist = 0;

  while (true) {
    let parent = null;
    let nearest = null;
    let dist = Infinity;

    for (const n in solutions) {
      if (!solutions[n]) continue;

      const ndist = solutions[n].dist;
      const adj = graph[n];

      for (const a in adj) {
        if (solutions[a]) continue;

        const d = adj[a] + ndist;

        if (d < dist) {
          parent = solutions[n];
          nearest = a;
          dist = d;
        }
      }
    }

    if (dist === Infinity) {
      break;
    }

    solutions[nearest] = parent.concat(nearest);
    solutions[nearest].dist = dist;
  }

  return solutions;
}

module.exports = dijkstra;
