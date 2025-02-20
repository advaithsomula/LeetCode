class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result= [0]*len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0]<temp:
                stackT, stackidx= stack.pop()
                result[stackidx]=idx-stackidx
            stack.append([temp, idx])
        return result
                



            
        