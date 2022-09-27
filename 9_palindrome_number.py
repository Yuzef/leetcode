class Solution:
    def isPalindrome_1(self, x: int) -> bool:
        x_str = str(x)
        x_str_rev = x_str[::-1]
        if x_str == x_str_rev:
            return True
        else:
            return False

    def isPalindrome_2(self, x: int) -> bool:  # Without converting the integer to a string
        if x < 0:
            return False  # optimization
        rvrsd = 0
        given_num = x

        while x != 0:
            last_digit = x % 10
            rvrsd = rvrsd * 10 + last_digit
            x = x // 10

        return given_num == rvrsd

print(Solution.isPalindrome_2(Solution, 123))


# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward.
#
# For example, 121 is a palindrome while 123 is not.
#
#
# Example 1:
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
# Constraints:
#
# -231 <= x <= 231 - 1
#
#
# Follow up: Could you solve it without converting the integer to a string?
