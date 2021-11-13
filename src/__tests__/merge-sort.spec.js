const mergeSort = require('../merge-sort');

describe('testing merge sort', () => {
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

  testCases.forEach(({ name, input, expected }) => {
    it(name, () => {
      const actual = mergeSort(input);
      expect(actual).toStrictEqual(input.sort((a, b) => a - b));
    });
  });
});
