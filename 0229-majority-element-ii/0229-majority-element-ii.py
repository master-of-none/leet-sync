class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)
        
        n = len(nums)
        res = []
        for val,count in hashmap.items():
            if count > n // 3:
                res.append(val)
        
        return res
