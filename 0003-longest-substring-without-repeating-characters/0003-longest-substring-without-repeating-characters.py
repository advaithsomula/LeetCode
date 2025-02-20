class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        max_length=0
        dict1=set()
        for right in range(len(s)):
            while s[right] in dict1:
                dict1.remove(s[left])
                left=left+1
            dict1.add(s[right])
            max_length=max(max_length,(right-left+1))
        return max_length
        