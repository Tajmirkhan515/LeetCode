#Given a sorted array of distinct integers and a target value, return the index if the target is #found. If not, return the index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def searchInsert(self, nums, target):

        first=0
        last=(len(nums)-1)
        print(last)
        while first<=last:
            mid=(first+last)//2
            
            if nums[mid]==target:
                return mid
            
            elif nums[mid]<target:            
                first=mid+1
            
            elif nums[mid]>target:
                last=mid-1
        return first