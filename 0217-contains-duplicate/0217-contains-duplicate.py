class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()

        for n in nums:
            if n in hashmap:
                return True
            
            hashmap.add(n) 
        
        return False
        