class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def bin_dec(string):
            return int(string,2)
        def dec_bin(num):
            return bin(num)[2:]
        
        total= bin_dec(a)+bin_dec(b)
        return dec_bin(total)
        