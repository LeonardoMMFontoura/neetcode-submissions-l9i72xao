class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        state = set()
        start = 0
        max_window = 0
        for end in range(len(s)):
            while s[end] in state:
                state.remove(s[start])
                start+=1
            state.add(s[end])
            max_window = max(max_window, end - start + 1)
        return max_window
