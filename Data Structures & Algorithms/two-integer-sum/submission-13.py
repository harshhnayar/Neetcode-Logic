class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_of = {}

        for i,num in enumerate(nums):
            needed = target - num
            if needed in index_of:
                return [index_of[needed], i]
            index_of[num] = i    