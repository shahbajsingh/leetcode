/*
Problem: Number of 1 Bits

Given a positive integer 'n', write a function that returns the number of set bits in 
its binary representation (also known as the Hamming weight).

Example 1:

Input: n = 11
Output: 3
Explanation:

The input binary string '1011' has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation:

The input binary string '10000000' has a total of one set bit.


Example 3:
Input: n = 2147483645
Output: 30
Explanation:

The input binary string '1111111111111111111111111111101' has a total of thirty set bits.

Constraints:

* 1 <= n <= 2^31 - 1

*/

#include <iostream>
using namespace std;

class Solution {
public:
    int hammingWeight(int n) {
        int count = 0;
        string binary = bitset<32>(n).to_string();
        for (int i=0; i < binary.length(); i++){
            if (binary[i] == '1'){
                count++;
            }
        }
        return count;
    }
};

int main() {
    Solution sol;
    cout << "Test 1: " << sol.hammingWeight(11) << endl; // Output: 3
    cout << "Test 2: " << sol.hammingWeight(128) << endl; // Output: 1
    cout << "Test 3: " << sol.hammingWeight(2147483645) << endl; // Output: 30
    return 0;
}