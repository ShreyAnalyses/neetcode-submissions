from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        result = []
        for val, freq in sorted(d.items(), key = lambda x: x[1], reverse = True):
            result.append(val)
            if len(result) == k: return result
