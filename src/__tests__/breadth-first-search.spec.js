const breadthFirstSearch = require('../breadth-first-search');

describe('testing breadth first search', () => {
  const testCases = [
    {
      name: 'should create a path',
      root: 1,
      tree: {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7]
      },
      expected: [1, 2, 3, 4, 5, 6, 7]
    },
    {
      name: 'should create a path avoiding duplicates',
      root: 1,
      tree: {
        1: [2, 3],
        2: [4, 6],
        3: [5, 6],
        4: [7, 8],
        5: [9, 10],
        6: [11, 12]
      },
      expected: [1, 2, 3, 4, 6, 5, 7, 8, 11, 12, 9, 10]
    }
  ];

  testCases.forEach(({ name, root, tree, expected }) => {
    it(name, () => {
      const actual = breadthFirstSearch(tree, root);
      expect(actual).toStrictEqual(expected);
    });
  });
});
