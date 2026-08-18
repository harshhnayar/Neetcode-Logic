class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d =  defaultdict(list)

        for i in strs:
            Ssort = "".join(sorted(i))
            d[Ssort].append(i)
        return list(d.values())      
