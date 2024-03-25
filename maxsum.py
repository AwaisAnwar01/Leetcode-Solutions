class Solution(object):
   def maxSubArray(self, nums):
        maxsum = nums[0]
        currentsum = nums[0]
        
        for R in range(1, len(nums)):
            if currentsum < 0:
                currentsum = nums[R]
            else:
                currentsum += nums[R]
            
            maxsum = max(currentsum, maxsum)
        
        return maxsum