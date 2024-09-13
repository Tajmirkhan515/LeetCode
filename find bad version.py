class Solution(object):
    def firstBadVersion(self, n):
        
        l=0
        h=n
        find=-1
        while l<=h:
            mid=(l+h)//2

            if isBadVersion(mid):
                find=mid
                h=mid-1
            else:
                l=mid+1
        
        return find