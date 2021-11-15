/**
 * Floyd–Warshall is an algorithm for finding shortest paths
 * in a directed weighted graph with positive or negative edge weights
 * (but with no negative cycles).
 *
 * Complexity: O(|V|^{3})
 */
function floydWarshall(graph) {
  const vertices = Object.keys(graph);
  const distances = {};

  vertices.forEach((vertex) => {
    distances[vertex] = {};
    vertices.forEach((vertex2) => {
      distances[vertex][vertex2] =
        vertex === vertex2 ? 0 : Number.POSITIVE_INFINITY;
    });
  });

  graph.forEach(([vertex1, vertex2, weight]) => {
    distances[vertex1][vertex2] = weight;
  });

  vertices.forEach((vertex1) => {
    vertices.forEach((vertex2) => {
      vertices.forEach((vertex3) => {
        distances[vertex1][vertex2] = Math.min(
          distances[vertex1][vertex2],
          distances[vertex1][vertex3] + distances[vertex3][vertex2]
        );
      });
    });
  });

  return distances;
}

module.exports = floydWarshall;
