
#2390. Removing Stars From a String

#You are given a string s, which contains stars *.

#In one operation, you can:

#Choose a star in s.
#Remove the closest non-star character to its left, as well as remove the star itself.
#Return the string after all stars have been removed.

#The input will be generated such that the operation is always possible.
#It can be shown that the resulting string will always be unique.

class Solution(object):
    def removeStars(self, s):
                
        result = []
        
        for char in s:
            if char == "*":
                # Remove the last character in result if '*' is found
                result.pop()
            else:
                result.append(char)
        
        # Join the list back into a string and return
        return "".join(result)
