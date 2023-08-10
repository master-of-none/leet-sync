class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for c in nums:
            if c == target:
                return True
        
        return False