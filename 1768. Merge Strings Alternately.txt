#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, #starting with word1. If a string is longer than the other, append the additional letters onto the #end of the merged string.

#Return the merged string.

class Solution(object):
    def mergeAlternately(self, word1, word2):

        ma=0

        if len(word1)>len(word2):
            ma= len(word1)
        else:
            ma=len(word2)
            
        merge=""    
        for x in range(ma):
            try:
                merge+=(word1[x])
            except:
                print(" ")
            try:
                merge+=(word2[x])
            except:
                print(" ")

        return merge