/**
 * Breadth–first search (BFS) is an algorithm for traversing or
 * searching tree or graph data structures.
 *
 * It starts at the tree root (or some arbitrary node of a graph,
 * sometimes referred to as a ‘search key’) and explores the
 * neighbor nodes first before moving to the next-level neighbors.
 *
 * Complexity: O(|V|+|E|) where V is a number of vertices in the graph
 * and E is a number of edges in the graph.
 */
function breadthFirstSearch(tree, node) {
  const queue = [node];
  const visited = new Set();
  const path = [];
  while (queue.length) {
    const current = queue.shift();
    if (visited.has(current)) continue;
    visited.add(current);
    path.push(current);
    const children = tree[current];
    if (!children) continue;
    children.forEach((child) => {
      if (!visited.has(child)) {
        queue.push(child);
      }
    });
  }

  return path;
}

module.exports = breadthFirstSearch;
