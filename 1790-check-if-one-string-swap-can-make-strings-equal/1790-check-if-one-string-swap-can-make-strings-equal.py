class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        c1 = []
        c2 = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                c1.append(s1[i])
                c2.append(s2[i])
        if len(c1) == 2:
            if(c1[0] == c2[1] and c2[0] == c1[1]):
                return True
        else:
            return False
        