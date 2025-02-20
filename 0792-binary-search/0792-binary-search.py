class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid= round(len(nums)/2)
        if nums[mid]==target:
            return mid
        if nums[mid]<target:
            for i in range(mid,len(nums)):
                if nums[i]==target:
                    return i
        if nums[mid]>target:
            for j in range(mid-1,-1,-1):
                if nums[j]==target:
                    return j
        if target not in nums:
            return -1
        
        