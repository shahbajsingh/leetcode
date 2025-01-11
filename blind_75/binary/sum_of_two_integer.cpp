/*
Problem: Sum of Two Integers

Given two integers 'a' and 'b', return the sum of the two integers without using the 
operators '+' and '-'.

Example:

Input: a = 1, b = 2
Output: 3

Example 2:

Input: a = 2, b = 3
Output: 5

Constraints:

* -1000 <= a, b <= 1000

*/

#include <iostream>
using namespace std;

class Solution {
public:
    int getSum(int a, int b) {
        while (b != 0) {
            int carry = a & b; // a AND b to calculate carry of binary addition
            a = a ^ b;         // a XOR b to calculate binary addition without carry
            b = carry << 1;    // left shift carry
        }

        return a;              // return a when b becomes zero
    }
};

int main() {
    Solution sol;
    cout << "2 + 2 = " << sol.getSum(1, 2) << endl; // 3
    cout << "2 + 3 = " << sol.getSum(2, 3) << endl; // 5
    return 0;
};