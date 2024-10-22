#334. Increasing Triplet Subsequence

#Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] #< nums[j] < nums[k]. If no such indices exists, return false.


# FIRST I USED THIS METHOD, BUT ITS NOT EFFIEIENT.
	i=0
        j=1
        k=2
        check=False
        while k<len(nums):
            
            if(nums[i]<nums[j]<nums[k]):
                check=True
                break
            i=j
            j=k
            k+=1
        return check



# THEN I CHANGED TO THIS, AFTER HELP FROM DIFFERENT SORUCES

class Solution(object):
    def increasingTriplet(self, nums):
        first = max(nums)
        second=max(nums)
        
        for num in nums:
            if num<=first:
                first=num
            elif num<=second:
                second=num
            else:
                return True

        return False       
        
        
        
        
