/*
Problem: Search in Rotated Sorted Array

There is an integer array 'nums' sorted in ascending order (with distinct
values).

Prior to being passed to your function, 'nums' is possibly rotated at an unknown
pivot index 'k' (1 <= k <= nums.length) such that the resulting array is
[nums[k], nums[k+1],
..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example,
[0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array 'nums' after the possible rotation and an integer 'target',
return the index of 'target' if it is in nums', or '-1' if it is not in 'nums'.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int> &nums, int target) {
        int n = nums.size();
        int left = 0, right = n - 1; // initialize left and right pointers

        // use binary search to find the pivot
        while (left <= right) {
            int mid = left + (right - left) / 2;

            // if target is found, return index
            if (nums[mid] == target) {
                return mid;
            }

            // if nums[left] <= nums[mid], then left half is sorted
            if (nums[left] <= nums[mid]) {
                // if target is in the left half
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }

            // if nums[mid] <= nums[right], then right half is sorted
            else {
                // if target is in the right half
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return -1; // target not found
    }
};

// TIME COMPLEXITY: O(log n)

int main() {
    Solution sol;
    vector<int> test1 = {4, 5, 6, 7, 0, 1, 2};

    cout << sol.search(test1, 0) << endl; // 4
    cout << sol.search(test1, 3) << endl; // -1

    return 0;
}