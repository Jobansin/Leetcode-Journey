class Solution(object):
    def groupAnagrams(self, strs):
        d= defaultdict(list)

        for s in strs:
            arr=[0]*26
            for c in s:
                arr[ord(c)-ord('a')]+=1
            d[tuple(arr)].append(s)
        return list(d.values())