/**
 * Quicksort is a divide-and-conquer algorithm.
 *
 * It works by selecting a 'pivot' element from the array
 * and partitioning the other elements into two sub-arrays,
 * according to whether they are less than or greater than the pivot.
 *
 * Complexity: O(n^2).
 */
function quickSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }

  const pivot = arr[0];
  const left = [];
  const right = [];

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < pivot) {
      left.push(arr[i]);
    } else {
      right.push(arr[i]);
    }
  }

  return [...quickSort(left), pivot, ...quickSort(right)];
}

module.exports = quickSort;
