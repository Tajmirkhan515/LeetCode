#1493. Longest Subarray of 1's After Deleting One Element

#Given a binary array nums, you should delete one element from it.

#Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

    def longestSubarray(self, nums):

        left = 0
        zero_count = 0
        max_len = 0
        
        # right pointer move
        for right in range(len(nums)):
            # If we encounter a zero
            if nums[right] == 0:
                zero_count += 1
            
            # If zero_count exceeds 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Calculate the length of the current window and update max_len.
            max_len = max(max_len, right - left + 1)
        
        
        return max_len -1
