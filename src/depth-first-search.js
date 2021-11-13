/**
 * Depth-first search (DFS) is an algorithm for traversing or searching
 * tree or graph data structures.
 *
 * The algorithm starts at the root node (selecting some arbitrary node
 * as the root node in the case of a graph) and explores as far as
 * possible along each branch before backtracking.
 *
 * Complexity: O(|V|+|E|) where V is a number of vertices in the graph
 * and E is a number of edges in the graph.
 */
function depthFirstSearch(tree, node) {
  return dfs(new Set(), tree, node);
}

function dfs(visited, tree, node) {
  const queue = [node];
  const path = [];
  while (queue.length) {
    const current = queue.shift();
    if (visited.has(current)) continue;
    visited.add(current);
    path.push(current);
    const children = tree[current];
    if (!children) continue;
    children.forEach((child) => {
      path.push(...dfs(visited, tree, child));
    });
  }
  return path;
}

module.exports = depthFirstSearch;
