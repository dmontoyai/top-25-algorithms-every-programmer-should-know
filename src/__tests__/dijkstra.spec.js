const dijkstra = require('../dijkstra');

describe('testing dijkstra algorithm', () => {
  const graph = {
    a: { e: 1, b: 1, g: 3 },
    b: { a: 1, c: 1 },
    c: { b: 1, d: 1 },
    d: { c: 1, e: 1 },
    e: { d: 1, a: 1 },
    f: { g: 1, h: 1 },
    g: { a: 3, f: 1 },
    h: { f: 1 }
  };
  const testCases = [
    {
      name: 'finding the shortest path fromm h to a',
      graph,
      source: 'h',
      to: 'a',
      expected: 5 // h =>(1) f =>(1) g =>(3) a
    },
    {
      name: 'finding the shortest path fromm a to h',
      graph,
      source: 'a',
      to: 'h',
      expected: 5 // a =>(3) g =>(1) f =>(1) h
    },
    ,
    {
      name: 'finding the shortest path fromm c to f',
      graph,
      source: 'c',
      to: 'f',
      expected: 6 //  c =>(1) b =>(1) a =>(3) g =>(1) f
    }
  ];

  testCases.forEach(({ name, graph, source, to, expected }) => {
    it(name, () => {
      const actual = dijkstra(graph, source);
      expect(actual[to].dist).toBe(expected);
    });
  });
});
