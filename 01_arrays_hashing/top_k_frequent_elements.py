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

        # REVIEW: PEP 8: `# comment` with a space. Comments should explain why, not what.
        # REVIEW: in interviews use `Counter(nums)` unless told not to.
        #Counter without using Counter
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        #Assign element to bucket
        for key, freq in counter.items():
            buckets[freq-1].append(key)

        # REVIEW: two counters (`to_pick`, `bucket_idx`) kept in sync invite off-by-one bugs.
        # Simpler: for freq in range(len(buckets) - 1, -1, -1): for num in buckets[freq]:
        # append, and return as soon as len(answer) == k.
        #Pick k from last
        to_pick = k
        bucket_idx = len(nums) - 1
        while to_pick > 0 and bucket_idx >= 0:
            bucket = buckets[bucket_idx]
            # REVIEW: `if bucket` is idiomatic; here the check isn't needed at all.
            if len(bucket) > 0:
                # REVIEW: slices clamp, so `bucket[:to_pick]` is enough; min() is
                # computed twice and is unnecessary.
                answer.extend(bucket[:min(len(bucket), to_pick)])
                to_pick -= min(len(bucket), to_pick)
            bucket_idx -= 1

        return answer
