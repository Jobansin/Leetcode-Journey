class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        l=0
        res=0
        for r in range (len(s)):
            window=r-l+1
            d[s[r]]=d.get(s[r], 0)+1
            if (window)-max(d.values()) > k:
                d[s[l]]-=1
                l+=1
            else:
                res=max(res, window)
        return res
