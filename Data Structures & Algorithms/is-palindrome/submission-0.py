class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ("".join(filter(str.isalnum, s))).lower()
        for i in range(len(s)//2):
            print(s[i], s[-i])
            if s[i] != s[-(i+1)]: return False
        return True
        