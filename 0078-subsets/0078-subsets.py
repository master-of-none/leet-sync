class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Left Side which will be included
            subset.append(nums[i])
            dfs(i+1)

            # Right Side which is not included
            subset.pop()
            dfs(i+1)

        dfs(0)

        return res 