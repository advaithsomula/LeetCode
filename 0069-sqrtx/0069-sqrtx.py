class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(0, 2**(31)-1):
            if x==i*i:
                return i
            if i*i<x<(i+1)*(i+1):
                return i
        