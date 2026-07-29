

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0

        if len(s) < 2:
            if p[0] == ".":
                return True
            else:
                if s[0] == p[0]:
                    return True

        while i < len(s):
            j = 0
            while j < len(p):
                if p[j] == "." and p[j + 1] == "*":
                    ...
                elif p[j] == "*":
                    ...
                else:
                    if s[i] != p[j]:
                        return False
        return True
