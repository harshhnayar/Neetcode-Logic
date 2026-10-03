class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexOf = {}

        for index,num in enumerate(nums):
            diff = target - num

            if diff in indexOf:
                return [indexOf[diff],index]
            indexOf[num] = index
        return []        