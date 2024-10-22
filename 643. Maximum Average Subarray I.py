#643. Maximum Average Subarray I

#You are given an integer array nums consisting of n elements, and an integer k.

#Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

class Solution(object):
    def findMaxAverage(self, nums, k):
        

        max_sum=sum(nums[:k])
      
        for i in range(k,len(nums)):
            current_sum=max_sum+nums[i]-nums[i-k]
            max_sum=max(max_sum,current_sum)
            
        

        return (max_sum*1.0)/k
