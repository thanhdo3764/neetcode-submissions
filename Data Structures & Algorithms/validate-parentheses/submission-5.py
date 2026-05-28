class Solution:
    def isValid(self, s: str) -> bool:
        closed_to_open = {')':'(', ']':'[', '}':'{'}
        idk = list()
        for bracket in s:
            if bracket not in closed_to_open:
                idk.append(bracket)
            else:
                if not idk: return False
                b = idk.pop(len(idk)-1)
                if closed_to_open[bracket] != b:
                    return False
        if idk: return False
        return True
        