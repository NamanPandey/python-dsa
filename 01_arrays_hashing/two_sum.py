"""Two Sum.

https://neetcode.io/problems/two-integer-sum

Approach: single pass with a value→index map; check the complement, then insert.
Time: O(n) · Space: O(n)
Alternatives: nested loops O(n²)/O(1); sort + two pointers loses original indices.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # REVIEW: misleading name: this is a dict. Use `index_of` or `seen`.
        # REVIEW: prefer the literal `{}` over `dict()`.
        num_set = dict()
        for idx, val in enumerate(nums):
            num_to_look = target - val
            if num_to_look in num_set:
                return [num_set[num_to_look], idx]
            # REVIEW: this does overwrite earlier indices (e.g. [3, 1, 3, 5], target 8).
            # Safe because any index holding that value is a valid partner.
            num_set[val] = idx
        # REVIEW: unreachable: the problem guarantees a solution. Say so in interviews.
        return []
