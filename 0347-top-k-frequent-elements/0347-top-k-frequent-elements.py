class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        arr=[]
        for i in nums:
            dict1[i]= dict1.get(i,0)+1
        sorted_array= sorted(dict1.items(), key= lambda x: x[1], reverse=True)

        for j in range(k):
            arr.append(sorted_array[j][0])

        return arr
            


        