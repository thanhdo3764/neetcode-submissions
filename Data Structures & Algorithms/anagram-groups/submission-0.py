class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        for s in strs:
            count = [0]*26
            for c in s: count[ord(c) - ord('a')] += 1
            if tuple(count) in ana: ana[tuple(count)].append(s)
            else: ana[tuple(count)] = [s]
            
        return [x for x in ana.values()]
        