class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = ""
        for n in digits:
            temp += str(n)
        
        temp = int(temp) + 1
        temp = str(temp)
        res = []
        for c in temp:
            res.append(int(c))
        
        return res