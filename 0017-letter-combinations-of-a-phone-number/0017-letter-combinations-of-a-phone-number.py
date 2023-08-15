class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digitsMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            
            for c in digitsMap[digits[i]]:
                backtrack(i+1, cur + c)
            
        
        if digits:
            backtrack(0, "")
        
        return res