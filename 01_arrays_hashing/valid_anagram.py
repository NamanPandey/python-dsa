"""Valid Anagram.

https://neetcode.io/problems/is-anagram

Approach: 26-slot count array; count s up, count t down with early exit.
Time: O(n) · Space: O(1)
Alternatives: compare two Counters O(n)/O(1); sort both O(n log n)/O(n).
Unicode follow-up: switch to a dict/Counter, O(k) space for k distinct characters.
"""

from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency = [0]*26

        for c in s:
            frequency[ord(c) - ord('a')] += 1

        for c in t:
            idx = ord(c) - ord('a')
            if frequency[idx] == 0:
                return False
            frequency[idx] -= 1

        for val in frequency:
            if val != 0:
                return False
        return True
