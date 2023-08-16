class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
          hashmap[i] = 1 + hashmap.get(i,0)
        
        for n,c in hashmap.items():
          freq[c].append(n)
        
        res = []
        for n in range(len(freq)-1, -1, -1):
          for c in freq[n]:
            res.append(c)
            if len(res) == k:
              return res