class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for char in s:
            if char in ['[', '{', '(']:
                l.append(char)
            if char in [']', '}', ')']:
                if l == []: return False

                elif char == ']' and l[-1] == '[': 
                    l = l[:len(l) - 1]
                elif char == '}' and l[-1] == '{': 
                    l = l[:len(l) - 1]
                elif char == ')' and l[-1] == '(': 
                    l = l[:len(l) - 1]
                else: return False

        if l!= []: return False
    

        return True
