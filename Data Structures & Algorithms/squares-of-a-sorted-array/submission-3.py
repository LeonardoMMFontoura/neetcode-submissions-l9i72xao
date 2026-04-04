class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        pos = len(nums) - 1
        res = [0] * len(nums)

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[pos] = nums[l] * nums[l]
                l += 1
            else:
                res[pos] = nums[r] * nums[r]
                r -= 1
            pos -= 1

        return res               