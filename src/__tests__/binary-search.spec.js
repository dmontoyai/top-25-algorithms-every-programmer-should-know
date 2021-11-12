const binarySearch = require('../binary-search');

describe('testing binary search', () => {
  const testCases = [
    {
      name: 'should find the element in log2(16) = 4 steps',
      input: Array.from({ length: 16 }, (_, i) => i),
      target: 0,
      expected: 4
    },
    {
      name: 'should find the element in log2(128) = 7 steps',
      input: Array.from({ length: 128 }, (_, i) => i),
      target: 0,
      expected: 7
    },
    {
      name: 'should find the element in log2(1024) = 10 steps',
      input: Array.from({ length: 1024 }, (_, i) => i),
      target: 0,
      expected: 10
    },
    {
      name: 'should find the element in log2(1048576) = 20 steps',
      input: Array.from({ length: 1048576 }, (_, i) => i),
      target: 0,
      expected: 20
    }
  ];

  testCases.forEach(({ name, input, target, expected }) => {
    it(name, () => {
      const actual = binarySearch(input, target);
      expect(actual).toBe(expected);
    });
  });
});
