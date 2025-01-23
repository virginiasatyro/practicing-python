'''
9. Palindrome number

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
'''

def checkBadNum(x):
    if x >= -2 ** 31 and x <= 2 ** 31 -1:
        return False
    return True

def isPalindrome(x):
    ''' solution: change the number from integer to string - easier to compare!'''
    if checkBadNum(x):
        return "Error: number out of range"
    s = str(x)
    return s == s[::-1]

def isPalindrome2(x):
    if checkBadNum(x):
        return "Error: number out of range"

    original = x
    reversed_num = 0
    while x > 0:
        reversed_num = reversed_num * 10 + x % 10
        x = x // 10
    return original == reversed_num
    
print(isPalindrome(121))
print(isPalindrome(12344321))
print(isPalindrome(123454321))
print(isPalindrome(-121))
print(isPalindrome(10))
