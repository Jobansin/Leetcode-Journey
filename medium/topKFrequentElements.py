class Solution(object):
    def topKFrequent(self, nums, k):
        d= defaultdict(int)
        arr= [[] for i in range(len(nums)+1)]
        
        for num in nums:
            d[num]= d.get(num, 0) + 1
        for num, count in d.items():
            arr[count].append(num)
        result=[]
        for i in range(len(arr)-1,0,-1):
            for nums in arr[i]:
                result.append(nums)
                if len(result) == k:
                    return result