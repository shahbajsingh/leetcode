/*
Problem: Maximum Product Subarray

Given an integer array 'nums', find a subarray that has the largest product, and return 
the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation:

[2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation:

The result cannot be 2, because [-2, -1] is not a subarray.

Constraints: 

* 1 <= nums.length <= 2 * 10^4

* -10 <= nums[i] <= 10

* The product of any subarray of 'nums' is guaranteed to fit in a 32-bit integer.

*/

#include <stdio.h>
#include <stdlib.h>

int maxProduct(int* nums, int numsSize) {
    int curr_max = nums[0]; // initialize curr_max
    int curr_min = nums[0]; // initialize curr_min
    int max_prod = nums[0]; // initialize max_prod

    for (int i = 1; i < numsSize; i++){
        if (nums[i] < 0) {
            // swap curr_max and curr_min when nums[i] is negative
            int temp = curr_max;
            curr_max = curr_min;
            curr_min = temp;
        }

        // if curr_max * nums[i] > nums[i], then update curr_max
        // else, update curr_max to nums[i]
        curr_max = (curr_max * nums[i] > nums[i]) ? curr_max * nums[i] : nums[i];


        // if curr_min * nums[i] < nums[i], then update curr_min
        // else, update curr_min to nums[i]
        curr_min = (curr_min * nums[i] < nums[i]) ? curr_min * nums[i] : nums[i];

        // update max_prod
        max_prod = (curr_max > max_prod) ? curr_max : max_prod;
    }

    return max_prod;
}

int main() {
    int test1[] = {2,3,-2,4};
    int test2[] = {-2,0,-1};

    printf("Test 1: %d\n", maxProduct(test1, 4)); // 6
    printf("Test 2: %d\n", maxProduct(test2, 3)); // 0

    return 0;
}