class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        c = collections.defaultdict()

        for i in range(len(numbers)):

            if (target - numbers[i]) in c:
                return [c[target - numbers[i]] + 1, i+1]

            else: 
                c[numbers[i]] = i