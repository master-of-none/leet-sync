class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for c in nums:
            if c in hashset:
                return True
            hashset.add(c)
        
        return False