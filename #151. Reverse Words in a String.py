#151. Reverse Words in a String

#Given an input string s, reverse the order of the words.

#A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

#Return a string of the words in reverse order concatenated by a single space.
#Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only
#have a single space separating the words. Do not include any extra spaces.

class Solution(object):
    def reverseWords(self, s):
        
        toList = s.split(" ")

        #remove spaces
        sl=[]
        for i in range(len(toList)):
            if toList[i] !='':
                sl.append(toList[i])
                

        # Initialize two pointers
        strptr = 0
        endptr = len(sl) - 1

        # Swap the words using the two pointers until they meet
        while strptr <= endptr:
            temp = sl[strptr]
            sl[strptr] = sl[endptr]
            sl[endptr] = temp
            strptr += 1
            endptr -= 1

        # Join the list back into a string
        reversed_s = " ".join(sl)
        return reversed_s
    
