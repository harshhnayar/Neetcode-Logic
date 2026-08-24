class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d =  defaultdict(list)

        for s in strs:
            sSort = "".join(sorted(s))
            d[sSort].append(s)
        return list(d.values())      