class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for r in range(len(nums)):
            if nums[r] in seen and abs(seen[nums[r]] - r) <= k:
                return True
            seen[nums[r]] = r
        return False
