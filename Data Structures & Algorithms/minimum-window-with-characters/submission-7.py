class Solution:
    def valid_substring(self, a, b):
        for k in b:
            if a[k] < b[k]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        freq = Counter(s)
        t = Counter(t)
        res = ""
        right = len(s)-1
        for left in range(len(s)):
            print(left, right)
            while not self.valid_substring(freq, t) and right < len(s) - 1:
                right += 1
                freq[s[right]] += 1
            if not self.valid_substring(freq, t): break
            while(True):
                freq[s[right]] -= 1
                if self.valid_substring(freq, t):
                    right -= 1
                else:
                    freq[s[right]] += 1
                    break
            if right - left + 1 < len(res) or res == "":
                res = s[left:right+1]
            freq[s[left]] -= 1
        return res
            
        