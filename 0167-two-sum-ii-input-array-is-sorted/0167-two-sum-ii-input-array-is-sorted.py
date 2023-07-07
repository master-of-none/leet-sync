class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            temp = numbers[l] + numbers[r]

            if temp < target:
                l += 1
            
            elif temp > target:
                r -= 1
            
            else:
                return [l+1, r+1]
