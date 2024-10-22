#724. Find Pivot Index

#Given an array of integers nums, calculate the pivot index of this array.

#The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

#If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

#Return the leftmost pivot index. If no such index exists, return -1.

class Solution(object):
    def pivotIndex(self, nums):
        # Total sum of all elements in nums
        total_sum = sum(nums)
        left_sum = 0

        # Loop through the array
        for i in range(len(nums)):
            # Calculate right sum as total_sum - left_sum - nums[i]
            right_sum = total_sum - left_sum - nums[i]
            
            # Check if left sum equals right sum
            if left_sum == right_sum:
                return i
            
            # Update left sum for the next iteration
            left_sum += nums[i]

        # If no pivot index is found, return -1
        return -1
