class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        nums = []
        for s in strs:
            nums.append(str(len(s)))
            nums_string = '_'.join(nums)
            prefix = nums_string + '__' + str(len(strs)) + '__' + ''.join(strs)
        return prefix
        
    def decode(self, s: str) -> List[str]:

        if s == "": return []
        parts = s.split('__', 2)
        nums_string, count_s, string = parts[0], parts[1], parts[2]
        nums_list = nums_string.split('_')

        idx = 0
        result = []
        for i in range(int(count_s)):
            word = string[idx: idx+int(nums_list[i])]
            result.append(word)
            idx += len(word)

        return result

