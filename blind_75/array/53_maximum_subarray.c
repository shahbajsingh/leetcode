/*
Problem: Maximum Subarray

Given an integer array 'nums', find the subarray with the largest sum, and return its sum

Example 1:

Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation:

The subarray [4, -1, 2, 1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation:

The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5, 4, -1, 7, 8]
Output: 23
Explanation:

The subarray [5, 4, -1, 7, 8] has the largest sum 23.

Constraints:

* 1 <= nums.length <= 10^5

* -10^4 <= nums[i] <= 10^4

Follow up: 

If you have figured out the O(n) solution, try coding another solution using the 
divide and conquer approach, which is more subtle.

*/

#include <stdio.h>
#include <stdlib.h>

int maxSubArray(int* nums, int numsSize) {
    int max_sum = nums[0]; // initialize max_sum
    int curr_sum = nums[0]; // initialize curr_sum

    for (int i = 1; i < numsSize; i++) {
        // if curr_sum + nums[i] > nums[i], then add nums[i] to curr_sum
        // else, update curr_sum to nums[i]
        curr_sum = (curr_sum + nums[i] > nums[i]) ? curr_sum + nums[i] : nums[i];

        // if curr_sum > max_sum, then update max_sum
        // else, continue to next iteration
        max_sum = (curr_sum > max_sum) ? curr_sum : max_sum;
    }

    return max_sum;
}

int main() {
    int test1[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int test2[] = {1};
    int test3[] = {5, 4, -1, 7, 8};

    printf("Test 1: %d\n", maxSubArray(test1, 9)); // 6
    printf("Test 2: %d\n", maxSubArray(test2, 1)); // 1
    printf("Test 3: %d\n", maxSubArray(test3, 5)); // 23

    return 0;
}

