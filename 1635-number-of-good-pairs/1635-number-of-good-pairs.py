class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = collections.defaultdict(int)
        res = 0

        for n in nums:
            res += hashmap[n]
            hashmap[n] += 1

        return res 