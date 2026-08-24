class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = Counter(nums)
        common = counted.most_common(k)
        found = []
        for i in common:
            found.append(i[0])
        return found    