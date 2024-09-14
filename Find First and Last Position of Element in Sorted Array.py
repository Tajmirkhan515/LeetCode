#Given an array of integers nums sorted in non-decreasing order, find the starting and ending #position of a given target value.

#If target is not found in the array, return [-1, -1].

#You must write an algorithm with O(log n) runtime complexity.


class Solution(object):
    def searchRange(self, nums, target):
        left = self.leftSide(nums, target)
        right = self.rightSide(nums, target)
        
        return [left, right]

    def leftSide(self, nums, target):
        l = 0  
        h = len(nums) - 1
        
        index = -1
        
        while l <= h:
            mid = (h + l) // 2  
            
            if nums[mid] == target:
                index = mid  
                h = mid - 1  # Continue to search on the left side
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        
        return index

    def rightSide(self, nums, target):
        l = 0  
        h = len(nums) - 1
        
        index = -1
        
        while l <= h:
            mid = (h + l) 
            
            if nums[mid] == target:
                index = mid  
                l = mid + 1  # Continue to search on the right side
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        
        return index
