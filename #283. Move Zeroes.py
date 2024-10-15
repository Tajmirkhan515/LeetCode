#283. Move Zeroes

#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#Note that you must do this in-place without making a copy of the array.

 class Solution(object):
    def moveZeroes(self, nums):
        startptr=0
        endptr=len(nums)-1
        while startptr<endptr:
           
            if nums[startptr]==0:
                temp=nums[startptr]
                j=startptr
                while j<endptr:            
                    nums[j]=nums[j+1]
                    j+=1
                    
                nums[endptr]=temp
                endptr-=1
            else:
                startptr+=1
        return nums
