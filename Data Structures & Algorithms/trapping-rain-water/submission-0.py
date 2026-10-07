class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        total_water = 0
        max_right = float("-inf")
        max_left = float("-inf")
        while left < right:
            max_right = max(max_right, height[right])
            max_left = max(max_left, height[left])
            if max_left >= max_right:
                total_water += max_right - height[right]
                right-=1
            elif max_right > max_left:
                total_water += max_left - height[left]
                left+=1
        return total_water
