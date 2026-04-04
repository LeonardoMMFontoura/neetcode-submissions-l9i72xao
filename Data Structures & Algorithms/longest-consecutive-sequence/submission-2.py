class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        best = 0
        for x in values:
            if (x - 1) not in values:
                curr = x
                length = 1
                while (curr + 1) in values:
                    curr += 1
                    length += 1
                best = max(best, length)
        return best