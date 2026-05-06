class Solution:

    def encode(self, strs: List[str]) -> str:
        count = len(strs)
        res = '\0'.join(strs)
        return f"{count}#{res}"

    def decode(self, s: str) -> List[str]:
        i = 0
        while s[i] != '#': i += 1
        if int(s[0:i]) == 0: return []
        s = s[i+1:]
        res = s.split('\0')
        return res
