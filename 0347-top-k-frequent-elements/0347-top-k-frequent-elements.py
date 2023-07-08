class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)
        
        for i,j in hashmap.items():
            freq[j].append(i)

        result = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
        