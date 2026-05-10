class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        filtered_str = ''.join(char for char in s if (char.isalnum()))
        return filtered_str == filtered_str[::-1]