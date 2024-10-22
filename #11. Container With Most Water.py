#11. Container With Most Water

#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

#Find two lines that together with the x-axis form a container, such that the container contains the most water.

#Return the maximum amount of water a container can store.

#Notice that you may not slant the container.

class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1

        final_max=0

        while left<right:
            max_area=min(height[left],height[right])*(right-left)
            final_max=max(max_area,final_max)
            
            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return final_max
        
        
