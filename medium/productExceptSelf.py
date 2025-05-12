class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1]*(len(nums)) #building the output array to be the size of nums array
        pre=1 #starting prefix because no number is to the left of (start of the array)
        post=1 #starting postfix because no number is to the right of (ending of the array)
        for i in range(len(nums)): #loop through by the length of nums
            output[i]*=pre #setting our output values each by our current prefix (at the start will always be 1)
            pre*=nums[i] #multiplying our prefix by the current index of nums we are on
        for i in range(len(nums)-1, -1, -1): #loop through by starting at length of nums -1, stopping at -1, going down by -1
            output[i]*=post #multiply our current output values (filled by prefix) by our current postfix (at the start will always be 1)
            post*=nums[i] #multiply our postfix by the the current index of nums we are on 
        return output #return our result
        """
        Returns an array where each element is the product of all other elements
        in nums, without using division.
        Time: O(n), Space: O(1) extra (output not counted).
        """
