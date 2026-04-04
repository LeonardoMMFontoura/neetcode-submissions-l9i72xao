class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = dict()
        for i, val in enumerate(nums):
            complement = target - val
            if complement in comps:
                return [comps[complement], i]
            comps[val] = i