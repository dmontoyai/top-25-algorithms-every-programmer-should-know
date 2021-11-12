/**
 * Given a sorted array of n integers and a target value,
 * determine if the target exists in the array in logarithmic
 * time using the binary search algorithm.
 *
 * If target exists in the array, print the index of it.
 *
 * Complexity:	O(log n) -> log2(n)
 */
function binarySearch(array, target) {
  let steps = 0;
  let lentgh = array.length;
  while (lentgh > 0) {
    const mid = Math.floor(lentgh / 2);
    if (array[mid] === target) {
      return steps;
    } else if (array[mid] > target) {
      steps++;
      lentgh = mid;
    } else {
      steps++;
      lentgh = lentgh - mid;
    }
  }
}

module.exports = binarySearch;
