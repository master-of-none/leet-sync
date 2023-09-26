class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [[] for i in range(len(nums) + 1)]
        hashmap = {}
        
        for n in nums:
          hashmap[n] = 1 + hashmap.get(n, 0)

        for n, c in hashmap.items():
          freq[c].append(n)
        
        for n in range(len(freq) - 1, 0 , -1):
          for c in freq[n]:
            res.append(c)

            if len(res) == k:
              return res