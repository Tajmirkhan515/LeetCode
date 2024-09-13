#Given an array of integers nums sorted in non-decreasing order, find the starting and ending #position of a given target value.

#If target is not found in the array, return [-1, -1].

#You must write an algorithm with O(log n) runtime complexity.


class Solution(object):
    def searchRange(self, nums, target):
        
        l=0
        h=(len(nums)-1)
        output=[-1,-1]
        index=0
        mid=0
        while l<=h:

            mid=(((l+h)//2)-1)

            if nums[mid]==target:
                output[index]=mid    
                print("mid id ",mid)                           
                index+=1
                if nums[mid+1]==target:
                    output[index]=mid+1
                elif nums[mid-1]==target:
                    output[index]=mid-1

                break
            elif nums[mid]<target:
                l=mid+1
            elif nums>target:
                h=mid-1


        return output