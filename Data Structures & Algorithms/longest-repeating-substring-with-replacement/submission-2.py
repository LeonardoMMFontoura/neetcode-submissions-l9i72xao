class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        count_s = {}
        max_freq = 0
        for right in range(len(s)):
            count_s[s[right]] = count_s.get(s[right], 0) + 1
            max_freq = max(max_freq, count_s[s[right]])
            while (right - left + 1) - max_freq > k:
                count_s[s[left]] -= 1 
                left+=1
            max_length = max(max_length, right - left + 1)
        return max_length
