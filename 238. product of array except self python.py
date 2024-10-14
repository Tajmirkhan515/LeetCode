

class Solution(object):
    def productExceptSelf(self, nums):
        #Here i get help from different sources
        
        n = len(nums)
        result = [1] * n

        # Calculate prefix products and store them in result
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Calculate suffix products on the fly and multiply with the prefix stored in result
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result

        
