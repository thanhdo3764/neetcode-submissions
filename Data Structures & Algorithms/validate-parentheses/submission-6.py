class Solution:
    def isValid(self, s: str) -> bool:
        closed_to_open = {')':'(', ']':'[', '}':'{'}
        idk = list()
        for bracket in s:
            if bracket not in closed_to_open:
                idk.append(bracket)
            else:
                if idk and idk[-1] == closed_to_open[bracket]:
                    idk.pop()
                else:
                    return False
        if idk: return False
        return True
        