class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        expected = defaultdict(int)
        consecutive_dict = defaultdict(int)
        for n in nums:
            key = n if not n in expected else expected[n]
            consecutive_dict[key] += 1
            expected[n+1] = key
            if n+1 in consecutive_dict:
                consecutive_dict[key] += consecutive_dict[n+1]
                expected[consecutive_dict[key]] = key
    
        return 0 if not consecutive_dict else max(consecutive_dict.values())
        