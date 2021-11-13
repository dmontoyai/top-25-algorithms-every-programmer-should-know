/**
 * Merge Sort is a Divide and Conquer algorithm, it divides a
 * large array into two smaller subarrays and then recursively
 * sort the subarrays.
 *
 * Complexity: O(nlog(n)).
 */
function mergeSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }

  const mid = Math.floor(arr.length / 2);
  const left = arr.slice(0, mid);
  const right = arr.slice(mid);
  return merge(mergeSort(left), mergeSort(right));
}

function merge(left, right) {
  const result = [];

  while (left.length && right.length) {
    if (left[0] < right[0]) {
      result.push(left.shift());
    } else {
      result.push(right.shift());
    }
  }
  return [...result, ...left, ...right];
}

module.exports = mergeSort;
