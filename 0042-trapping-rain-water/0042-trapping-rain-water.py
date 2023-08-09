class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        leftMax = height[l]
        rightMax = height[r]
        area=0

        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(height[l], leftMax)
                area += leftMax - height[l]
            
            else:
                r-=1
                rightMax = max(height[r], rightMax)
                area += rightMax - height[r]
        
        return area