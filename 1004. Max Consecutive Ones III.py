#1004. Max Consecutive Ones III
#Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

class Solution(object):
    def longestOnes(self, nums, k):
        left=0
        max_length=0
        zero_count=0

        for right in range(len(nums)):
            if nums[right]==0:
                zero_count+=1
            
            while zero_count>k:
                if nums[left]==0:
                    zero_count-=1
                left+=1
            max_length=max(max_length,right-left+1)

        return max_length
        
