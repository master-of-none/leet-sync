class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        hashset = set(nums)

        for i in range(1, len(nums)+1):
            if i not in hashset:
                res.append(i)

        return res            