"""Contains Duplicate.

https://neetcode.io/problems/duplicate-integer

Approach: hash set of seen values; return True on the first repeat.
Time: O(n) · Space: O(n)
Alternatives: nested loops O(n²)/O(1); sort + compare neighbours O(n log n) (mutates input).
"""

from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        return False
