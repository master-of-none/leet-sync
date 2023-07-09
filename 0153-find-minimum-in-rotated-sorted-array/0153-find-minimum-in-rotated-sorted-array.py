class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = nums[0]

        for i in range(len(nums)):
            mini = min(nums[i],mini)
        
        return mini