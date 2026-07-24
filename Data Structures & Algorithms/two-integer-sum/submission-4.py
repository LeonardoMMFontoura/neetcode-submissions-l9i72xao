class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for k,v in enumerate(nums):
            complement = target - v
            if complement in hashmap:
                return [hashmap[complement], k]
            hashmap[v] = k
