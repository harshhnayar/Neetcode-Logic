class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            sortedStr = "".join(sorted(i))
            if sortedStr not in d:
                d[sortedStr] = []
            
            d[sortedStr].append(i)  
                 
        return list(d.values())        
