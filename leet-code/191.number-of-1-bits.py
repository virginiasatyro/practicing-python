'''
191. Number of 1 Bits

Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight - https://en.wikipedia.org/wiki/Hamming_weight).


Example 1:

Input: n = 11
Output: 3

Explanation:
The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128
Output: 1

Explanation:
The input binary string 10000000 has a total of one set bit.

Example 3:
Input: n = 2147483645
Output: 30

Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

Constraints:

1 <= n <= 231 - 1

Follow up: If this function is called many times, how would you optimize it?

'''

def hammingWeight(n: int) -> int:
    ''' bin return an string representation of the binary value of n:
        bin(3) -> 0b11
        count will count the number of 1s in the string
        Attention! if you count the number of 0s, you will get the number 0b also.
    '''
    if n >= 1 and n <= 2**31 -1:
        return bin(n).count('1')
    else:
        return "Error: n must be between 1 and 231 - 1"

print(hammingWeight(11)) # 3
print(hammingWeight(128)) # 1
print(hammingWeight(2147483645)) # 30
print(hammingWeight(-10)) # Error