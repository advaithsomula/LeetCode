class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1=defaultdict(list)
        for i in strs:
            word="".join(sorted(i))
            dict1[word].append(i)
        return list(dict1.values())
        
        