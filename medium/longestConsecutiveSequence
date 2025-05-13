class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset= set(nums)
        counter=0
        for num in numset:
            if num-1 not in numset:
                current=1
                while num+current in numset:
                    current+=1
                counter= max(counter, current)
        return counter
