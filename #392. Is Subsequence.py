#392. Is Subsequence


#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

#A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution(object):
    def isSubsequence(self, s, t):
        if len(s)==0:
            return True
        index=0

        for i in range(len(t)):
            if t[i]==s[index]:
                index+=1
                if index==len(s):
                    return True
        return False
        
