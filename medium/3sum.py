class Solution(object):
    def threeSum(self, nums):
        arr=[]
        sn=sorted(nums)
        for i in range(len(sn)):
            if sn[i] > 0:
                break
                
            if i>0 and sn[i]==sn[i-1]:
                continue

            L=i+1
            R=len(sn)-1
            while L < R:
                if sn[L]+sn[R]+sn[i]<0:
                    L+=1
                elif sn[L]+sn[R]+sn[i]>0:
                    R-=1
                else:
                    arr.append([sn[i],sn[L],sn[R]])
                    L+=1
                    R-=1
                    while sn[L] == sn[L-1] and L<R:
                        L+=1
                    while sn[R] == sn[R+1] and R>L:
                        R-=1
        return arr
