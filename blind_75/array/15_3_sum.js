/*
Problem: 3 Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:

nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

The distinct triplets are [-1,0,1] and [-1,-1,2]. Notice that the order of the output 
and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation:

The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0,
Output: [[0,0,0]]
Explanation:

The only possible triplet sums up to 0.

Constraints:

* 3 <= nums.length <= 3000
* -10^5 <= nums[i] <= 10^5
*/

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    // sort the array
    nums.sort((a, b) => a - b);

    const result = [];
    const n = nums.length;

    // loop through the array
    for (let i = 0; i < n; i++) {
        // check for duplicates
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue;
        }

        // initialize left and right pointers
        let left = i + 1;
        let right = n - 1;

        // loop through the array
        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];

            // if sum is 0, add to result
            if (sum === 0) {
                result.push([nums[i], nums[left], nums[right]]);

                // check for duplicates
                while (left < right && nums[left] === nums[left + 1]) {
                    left++;
                }

                // check for duplicates
                while (left < right && nums[right] === nums[right - 1]) {
                    right--;
                }

                left++;
                right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }

    return result;
};

// TIME COMPLEXITY: O(n^2)

// test cases

console.log(threeSum([-1,0,1,2,-1,-4])); // [[-1,-1,2],[-1,0,1]]
console.log(threeSum([0,1,1])); // []
console.log(threeSum([0,0,0])); // [[0,0,0]]