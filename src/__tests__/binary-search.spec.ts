const binarySearch = require('../binary-search');

describe('testing binary search', () => {
  it('should find the index of the item in the array in 2 steps', () => {
    const actual = binarySearch(Array.from({ length: 4 }), 3);
    const expected = 0;

    expect(actual).toEqual(expected);
  });

  it('should find the index of the item in the array in 2 steps', () => {
    const actual = binarySearch(Array.from({ length: 1000 }), 500);
    const expected = 500;

    expect(actual).toBeLessThanOrEqual(expected);
  });
});
