#344. Reverse String

#Write a function that reverses a string. The input string is given as an array of characters s.

#You must do this by modifying the input array in-place with O(1) extra memory.


#solution
class Solution(object):
    def reverseString(self, s):
        
        strptr=0
        endptr=(len(s)-1)

        while strptr<endptr:
            temp=s[strptr]
            s[strptr]=s[endptr]
            s[endptr]=temp
            strptr+=1
            endptr-=1
        
        return s
        
