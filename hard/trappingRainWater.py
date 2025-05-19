class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        l=0
        r=len(height)-1
        lmax=0
        rmax=0
        water=0
        while l<r:
            count=0
            if height[l]<height[r]:
                count=lmax-height[l]
                lmax=max(lmax, height[l])
                l+=1
            else:
                count=rmax-height[r]
                rmax=max(rmax, height[r])
                r-=1
            if count>0:
                water+=count
        return water