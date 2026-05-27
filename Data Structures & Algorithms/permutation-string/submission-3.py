class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x = sorted(s1)
        for idx in range(len(s2) + 1 -len(s1)):
            ss = s2[idx : idx + len(s1)]
            if sorted(ss) == x : return True

        return False
        