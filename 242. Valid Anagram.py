#242. Valid Anagram
#Given two strings s and t, return true if t is an 
#anagram
# of s, and false otherwise.
 #Example 1:
#Input: s = "anagram", t = "nagaram"
#Output: true


from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s)==Counter(t)

        countS=Counter(s)
        countT=Counter(t)

        for term in countT:
            if countS[term]!=countT[term]:
                return False
        
        return True
