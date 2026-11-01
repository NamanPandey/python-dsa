"""Two Sum.

https://neetcode.io/problems/two-integer-sum

Approach: single pass with a value→index map; check the complement, then insert.
Time: O(n) · Space: O(n)
Alternatives: nested loops O(n²)/O(1); sort + two pointers loses original indices.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = dict()
        for idx, val in enumerate(nums):
            num_to_look = target - val
            if num_to_look in num_set:
                return [num_set[num_to_look], idx]
            num_set[val] = idx
        return []
