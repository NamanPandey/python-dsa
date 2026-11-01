"""Top K Frequent Elements.

https://neetcode.io/problems/top-k-elements-in-list

Approach: count frequencies, bucket numbers by frequency, collect from the highest bucket down.
Time: O(n) · Space: O(n)
Alternatives: sort counts O(n log n); size-k min-heap O(n log k) time, best for streaming data.
"""

from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums))]
        answer = []

        #Counter without using Counter
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        #Assign element to bucket
        for key, freq in counter.items():
            buckets[freq-1].append(key)

        #Pick k from last
        to_pick = k
        bucket_idx = len(nums) - 1
        while to_pick > 0 and bucket_idx >= 0:
            bucket = buckets[bucket_idx]
            if len(bucket) > 0:
                answer.extend(bucket[:min(len(bucket), to_pick)])
                to_pick -= min(len(bucket), to_pick)
            bucket_idx -= 1

        return answer
