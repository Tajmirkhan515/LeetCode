#844. Backspace String Compare

#Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

#Note that after backspacing an empty text, the text will continue empty.
#Example 1:
#Input: s = "ab#c", t = "ad#c"
#Output: true
#Explanation: Both s and t become "ac".

class Solution(object):
    def backspaceCompare(self, s, t):
        
        sLst=[]
        tLst=[]

        for c in s:
            if c=="#":
                if len(sLst)!=0:
                    sLst.pop()
            else:
                sLst.append(c)    

        for c in t:
            if c=="#":
                if len(tLst)!=0:                
                    tLst.pop()
            else:
                tLst.append(c)        
        
        s="".join(sLst)
        t="".join(tLst)                

        if s==t:
            return True
        else:
            return False    
