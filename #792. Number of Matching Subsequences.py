#792. Number of Matching Subsequences

#Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

#A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

#For example, "ace" is a subsequence of "abcde".

class Solution(object):
    def numMatchingSubseq(self, s, words):
        substring=0
        for w in words:
            index=0    
            for i in range(len(s)):
                if s[i]==w[index]:
                    index+=1
                    if index==len(w):                
                        substring+=1
                        break
        return substring
