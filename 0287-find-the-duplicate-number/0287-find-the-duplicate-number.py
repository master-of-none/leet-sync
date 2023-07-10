class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashset = set()

        for n in nums:
            if n in hashset:
                return n
            
            hashset.add(n)
        