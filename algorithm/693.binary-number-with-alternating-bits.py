#
# @lc app=leetcode id=693 lang=python
#
# [693] Binary Number with Alternating Bits
#
# https://leetcode.com/problems/binary-number-with-alternating-bits/description/
#
# algorithms
# Easy (57.64%)
# Total Accepted:    38.7K
# Total Submissions: 67.1K
# Testcase Example:  '5'
#
# Given a positive integer, check whether it has alternating bits: namely, if
# two adjacent bits will always have different values.
#
# Example 1:
#
# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101
#
#
#
# Example 2:
#
# Input: 7
# Output: False
# Explanation:
# The binary representation of 7 is: 111.
#
#
#
# Example 3:
#
# Input: 11
# Output: False
# Explanation:
# The binary representation of 11 is: 1011.
#
#
#
# Example 4:
#
# Input: 10
# Output: True
# Explanation:
# The binary representation of 10 is: 1010.
#
#
#


class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mask = 0b10
        if n & 1 == 1:
            n = n >> 1
        while n:
            temp = (n >> 2 << 2) + mask
            if temp ^ n != 0:
                return False
            n = n >> 2
        return True
