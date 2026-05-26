class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        window = set()
        for i, c in enumerate(s):
            print(window)
            while c in window and left < i:
                window.remove(s[left])
                left += 1
            window.add(c)
            longest = max(longest, i - left + 1)
        
        return longest




        