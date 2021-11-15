const kruskal = require('../kruskal');

describe('testing floyd warshall', () => {
  const testCases = [
    {
      name: 'finds a minimum spanning forest in a small graph',
      nodes: ['A', 'B', 'C'],
      edges: [
        ['A', 'B', 1],
        ['B', 'C', 2],
        ['C', 'D', 3]
      ],
      expected: [
        ['A', 'B', 1],
        ['B', 'C', 2]
      ]
    },
    {
      name: 'finds a minimum spanning forest in a large graph',
      nodes: ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
      edges: [
        ['A', 'B', 7],
        ['A', 'D', 5],
        ['B', 'C', 8],
        ['B', 'D', 9],
        ['B', 'E', 7],
        ['C', 'E', 5],
        ['D', 'E', 15],
        ['D', 'F', 6],
        ['E', 'F', 8],
        ['E', 'G', 9],
        ['F', 'G', 11]
      ],
      expected: [
        ['C', 'E', 5],
        ['A', 'D', 5],
        ['D', 'F', 6],
        ['B', 'E', 7],
        ['A', 'B', 7],
        ['E', 'F', 8],
        ['B', 'C', 8],
        ['E', 'G', 9]
      ]
    }
  ];

  testCases.forEach(({ name, nodes, edges, expected }) => {
    it(name, () => {
      const actual = kruskal(nodes, edges);
      expect(actual).toStrictEqual(expected);
    });
  });
});
