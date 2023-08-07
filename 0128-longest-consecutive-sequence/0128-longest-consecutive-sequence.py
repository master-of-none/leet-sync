class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        result = set(nums)
        longest = 0

        for n in nums:
            if n-1 not in result:
                length = 0

                while n+length in result:
                    length+=1
                
                longest = max(longest, length)
        
        return longest