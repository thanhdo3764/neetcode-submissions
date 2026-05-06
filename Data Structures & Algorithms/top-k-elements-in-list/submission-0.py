class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        sorted_freq = sorted([(v,k) for k,v in count.items()], reverse=True)
        return [sorted_freq[i][1] for i in range(k)]

        