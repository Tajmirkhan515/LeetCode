#345. Reverse Vowels of a String

#Given a string s, reverse only all the vowels in the string and return it.

#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


#solution
class Solution(object):
    def reverseVowels(self, s):

        v=[]
        vowel="aAEeIiUuOo"
        for i in range(len(s)):
            if s[i] in vowel:        
                v.append(s[i])

        vowelLI=(len(v)-1)

        strL=list(s)

        for i in range(len(s)):
            if strL[i] in vowel:        
                strL[i]=v[vowelLI]
                vowelLI-=1

        s = "".join(strL)

        return s
