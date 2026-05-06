class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        res = []
        for i in range(len(nums)):
            if i == 0: prefix.append(1)
            else:
                prefix.append(prefix[i-1] * nums[i-1])
        
        for i in range(len(nums)):
            if i == 0: suffix.append(1)
            else:
                suffix.insert(0, suffix[-i] * nums[-(i)])

        print(prefix)
        print(suffix)

        return [prefix[i]*suffix[i] for i in range(len(nums))]
        