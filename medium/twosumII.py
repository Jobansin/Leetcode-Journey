class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(numbers)):
            result=target-numbers[i]
            if result in d:
                return [(d[result])+1, i+1]
            d[numbers[i]]=i
