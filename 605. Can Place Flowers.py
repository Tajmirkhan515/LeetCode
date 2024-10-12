
605. Can Place Flowers
Easy
Topics
Companies
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        for i in range(len(flowerbed)):
            if n==0:
                break  
                
            prev=0
            next=0
            if flowerbed[i]==0:

                if i==0 or flowerbed[i-1]==0:
                    prev=0
                else:
                    prev=1
                
                if i==(len(flowerbed)-1) or flowerbed[i+1]==0:
                    next=0
                else:
                    next=1
                    
                if prev==0 and next==0:
                    flowerbed[i]=1
                    n-=1
              

        if n==0:
            return True
        else:
            return False
        
