class Solution(object):
    def twoSum(self, nums, target):
        hashmap={}
        for i in range(len(nums)):
            result=target-nums[i]
            if result in hashmap:
                return [hashmap[result], i]
            hashmap[nums[i]]=i