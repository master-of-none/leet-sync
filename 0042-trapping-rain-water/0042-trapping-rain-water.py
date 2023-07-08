class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        res = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(height[l], leftMax)
                res += leftMax - height[l]

            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                res += rightMax - height[r]

        return res 