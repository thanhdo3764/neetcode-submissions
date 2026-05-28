class Solution:
    def findMin(self, nums: List[int]) -> int:
        minn = float('infinity')
        low = 0
        high = len(nums) - 1

        while low <= high:
            
            mid = (low + high) // 2
            print(mid)
            minn = min(minn, nums[mid])
        
            if nums[mid] < nums[low] or nums[mid] < nums[high]:
                high = mid - 1
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                break
        return minn