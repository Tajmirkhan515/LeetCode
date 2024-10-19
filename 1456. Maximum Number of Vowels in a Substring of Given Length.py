1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

class Solution(object):
    def maxVowels(self, s, k):
        lst=list(s)
        vowel={'a','e','i','o','e','u'}
        temp_cout=0
        r=k-1
        max_sub=0
        i=0
        while i<=(len(lst)-1):
            if lst[i] in vowel:
                temp_cout+=1
            if i==r:
                max_sub=max(max_sub,temp_cout)
                temp_cout=0
                r+=k
            i+=1
        return max_sub
