#541. Reverse String II

#Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

#If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

class Solution(object):
    def reverseStr(self, s, k):

        l=list(s)
        m=k

        def reverse(i,k):

            strptr=i
            endptr=k
            while strptr<endptr:
                temp=l[strptr]
                l[strptr]=l[endptr]
                l[endptr]=temp
                strptr+=1
                endptr-=1
                



        i=0
        iteration=0
        while i<len(l):
            if iteration%2==0:        
                reverse(i,k-1)
            iteration+=1
            a=k
            i=k
            k=k+2
            if (k-1)==len(s):
                break

        return "".join(l)


        
