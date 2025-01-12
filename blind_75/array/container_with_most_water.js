/*
Problem: Container With Most Water

You are given an integer array 'height' of length 'n'. There are 'n' vertical lines 
drawn such that the two endpoints of the 'i'th line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container 
contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: 

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, 
the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

Constraints:

* n == height.length

* 2 <= n <= 105

* 0 <= height[i] <= 104

*/

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let left = 0; // initialize left pointer
    let right = height.length - 1; // initialize right pointer
    let maxArea = 0; // initialize max volume variable

    while (left < right) { 
        // calculate current area
        const currHeight = Math.min(height[left], height[right]);
        const width = right - left;
        const currArea = currHeight * width;

        // update maxArea if currArea > maxArea
        maxArea = Math.max(maxArea, currArea);

        // move pointer for shorter line inward
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return maxArea;
};

// TIME COMPLEXITY: O(n)

console.log(maxArea([1,8,6,2,5,4,8,3,7])); // 49
console.log(maxArea([1,1])); // 1