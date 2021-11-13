const depthFirstSearch = require('../depth-first-search');

describe('testing depth first search', () => {
  const testCases = [
    {
      name: 'should create a path of two levels',
      root: 1,
      tree: {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7]
      },
      expected: [1, 2, 4, 5, 3, 6, 7]
    },
    {
      name: 'should create a path of 3 levels avoiding duplicates',
      root: 1,
      tree: {
        1: [2, 3],
        2: [4, 6],
        3: [5, 6],
        4: [7, 8],
        5: [9, 10],
        6: [11, 12]
      },
      expected: [1, 2, 4, 7, 8, 6, 11, 12, 3, 5, 9, 10]
    }
  ];

  testCases.forEach(({ name, root, tree, expected }) => {
    it(name, () => {
      const actual = depthFirstSearch(tree, root);
      expect(actual).toStrictEqual(expected);
    });
  });
});
