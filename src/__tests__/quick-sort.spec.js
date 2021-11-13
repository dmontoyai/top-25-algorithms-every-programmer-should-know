const quickSort = require('../quick-sort');

describe('testing quick sort', () => {
  const testCases = [
    {
      name: 'should sort a small array',
      input: [10, 5, 1, 3]
    },
    {
      name: 'should sort a medium array',
      input: Array.from({ length: 128 }, () => Math.floor(Math.random() * 128))
    },
    {
      name: 'should sort a big array',
      input: Array.from({ length: 1024 }, () =>
        Math.floor(Math.random() * 1024)
      )
    }
  ];

  testCases.forEach(({ name, input }) => {
    it(name, () => {
      const actual = quickSort(input);
      expect(actual).toStrictEqual(input.slice().sort((a, b) => a - b));
    });
  });
});
