class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()

        i = len(nums)-1

        while k > 0:
            res = nums[i]
            i-=1
            k-=1
        
        return res