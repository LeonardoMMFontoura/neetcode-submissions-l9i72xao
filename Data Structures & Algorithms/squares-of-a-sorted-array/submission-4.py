class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        pos = len(nums) - 1
        while left <= right:
            square1 = nums[left] * nums[left]
            square2 = nums[right] * nums[right]
            if square1 < square2:
                squared[pos] = square2
                right-=1
            else:
                squared[pos] = square1
                left+=1
            pos-=1
        return squared 