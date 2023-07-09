class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        result = [0] * len(temp)
        stack = []

        for i, t in enumerate(temp):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = i - stackInd
            
            stack.append([t,i])
        
        return result