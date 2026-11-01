"""Group Anagrams.

https://neetcode.io/problems/anagram-groups

Approach: defaultdict(list) keyed by a 26-count signature.
Time: O(n·k) · Space: O(n·k)  (n strings, average length k)
Alternatives: sorted-string key O(n·k log k), often faster in CPython because sorting runs in C.
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # REVIEW: PEP 8 snake_case: `anagram_key`, not `createHashKey`.
        def createHashKey(s: str) -> str:
            # REVIEW: name by content: `counts`, not `hash_list`.
            hash_list = [0]*26
            for c in s:
                hash_list[ord(c) - ord('a')] += 1

            # REVIEW: `return tuple(hash_list)` is hashable, collision-free and
            # skips 26 str() conversions. The separator here is what prevents
            # [1, 11] vs [11, 1] colliding; never drop it from a string key.
            return "|".join(map(str, hash_list))

        # REVIEW: name by intent: `groups`, not `dictionary`.
        dictionary = defaultdict(list)
        for word in strs:
            dictionary[createHashKey(word)].append(word)

        return list(dictionary.values())
