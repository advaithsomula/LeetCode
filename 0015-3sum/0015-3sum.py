class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        tot=0
        for i in range(n-2):
            low=i+1
            high=n-1
            while low<high:
                tot=nums[i]+nums[low]+nums[high]
                if tot==0:
                    k=[nums[i],nums[low],nums[high]]
                    if k not in ans:
                        ans.append(k)
                    low+=1
                    high-=1
                elif tot<0:
                    low+=1
                else:
                    high-=1
        return ans
                    
                    
        