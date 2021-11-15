const _ = require('underscore');

/**
 * Kruskal's is an algorithm that finds a minimum spanning forest
 * of an undirected edge-weighted graph.
 *
 * If the graph is connected, it finds a minimum spanning tree.
 *
 * Complexity: O(E log2(V)), being V the number of vertices
 */

function kruskal(nodes, edges) {
  const minimumSpanningForest = [];
  let forest = nodes.map((node) => [node]);
  const sortedEdges = _.sortBy(edges, (edge) => -edge[2]);

  while (forest.length > 1) {
    const edge = sortedEdges.pop();
    const n1 = edge[0];
    const n2 = edge[1];

    const t1 = forest.filter((tree) => _.include(tree, n1));
    const t2 = forest.filter((tree) => _.include(tree, n2));

    if (t1 != t2) {
      forest = _.without(forest, t1[0], t2[0]);
      forest.push(_.union(t1[0], t2[0]));
      minimumSpanningForest.push(edge);
    }
  }
  return minimumSpanningForest;
}
module.exports = kruskal;
