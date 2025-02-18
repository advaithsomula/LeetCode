class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length= len(nums)
        product=[1]*length
        for i in range(1, length):
            product[i]= product[i-1]*nums[i-1]

        right=nums[-1]
        for j in range(length-2, -1, -1):
            product[j]=product[j]*right
            right=right*nums[j]
        return product



                