#2215. Find the Difference of Two Arrays
#Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

#answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
#answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
#Note that the integers in the lists may be returned in any order.

class Solution(object):
    def findDifference(self, nums1, nums2):
        set1=set(nums1)
        set2=set(nums2)

        res1=[]
        res2=[]


        for n in set1:
            if n not in set2:
                res1.append(n)
                
                
        for n in set2:
            if n not in set1:
                res2.append(n)   
        
        return [res1,res2]
