#443. String Compression


#Given an array of characters chars, compress it using the following algorithm:

#Begin with an empty string s. For each group of consecutive repeating characters in chars:

#If the group's length is 1, append the character to s.
#Otherwise, append the character followed by the group's length.
#The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

#After you are done modifying the input array, return the new length of the array.

#You must write an algorithm that uses only constant extra space.

class Solution(object):
    def compress(self, chars):
        s=1
        last=chars[0]
        writeIndex=1
        if len(chars)==1:
            return writeIndex
        for i in range(1,len(chars)):
            if last==chars[i]:
                s+=1
                last=chars[i]
                #if s>2:
                #    chars.pop(i)
            else:        
                if s>=2:
                                
                    for c in str(s):
                        print(c)
                        print("Index:",writeIndex)
                        
                        chars[writeIndex]=c
                        writeIndex+=1
                chars[writeIndex] = chars[i]
                writeIndex+=1
                last=chars[i]
                s=1
        if s>=2:     
               
            for c in str(s):                       
                chars[writeIndex]=str(c)
                writeIndex+=1
           
        return writeIndex
        
