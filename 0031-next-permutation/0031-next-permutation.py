class Solution:
    def upper(self,start,end,nums,target):
        res = start
        while start<=end:
            mid = (start+end)//2
            if nums[mid]>target:
                res = mid
                start = mid+1
            else:
                end = mid-1
        return res
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums)==1:
            return
        i = len(nums)-2
        j = i+1
        while i>=0:
            if nums[i]<nums[j]:
                up = self.upper(j,len(nums)-1,nums,nums[i])
                nums[i],nums[up]=nums[up],nums[i]
                nums[j:] = sorted(nums[j:])
                return
            i-=1
            j-=1
        nums.sort()
        return
        

        