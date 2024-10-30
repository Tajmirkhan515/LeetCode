
#1047. Remove All Adjacent Duplicates In String
#You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
#We repeatedly make duplicate removals on s until we no longer can.
#Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

#Example 1:
#Input: s = "abbaca" Output: "ca" 

#Example 2:
#Input: s = "azxxzy" Output: "ay" 

class Solution(object):
    def removeDuplicates(self, s):
        
        result=[]
         for c in s:
            if result and result[-1]==c:
                result.pop()
            else:
                result.append(c)
        return "".join(result) 

