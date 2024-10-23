#1207. Unique Number of Occurrences

#Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

class Solution(object):
    def uniqueOccurrences(self, arr):
        dec={}
        for n in arr:
            dec[n]=(dec.get(n, 0)+1)

            
        occur = dec.values()
        return len(occur) == len(set(occur))
