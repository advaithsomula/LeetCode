class Solution:
    def maxArea(self, height: List[int]) -> int:
        result=0
        l,r= 0, len(height)-1
        while(l<r):
            area=(r-l)*(min(height[l],height[r]))
            result=max(result,area)
            
            if(height[l]<height[r]):
                l=l+1
            else:
                r=r-1
        return result
            
        