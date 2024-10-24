#1657. Determine if Two Strings Are Close

#Two strings are considered close if you can attain one from the other using the following operations:

#Operation 1: Swap any two existing characters.
#For example, abcde -> aecdb
#Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
#For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
#You can use the operations on either string as many times as necessary.

#Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

class Solution(object):
    def closeStrings(self, word1, word2):
        
        set1=set(word1)
        set2=set(word2)

        if set1!=set2:
            return False
        
        freq1=[word1.count(char) for char in set1]
        freq2=[word2.count(char) for char in set2]

        return sorted(freq1)==sorted(freq2)
