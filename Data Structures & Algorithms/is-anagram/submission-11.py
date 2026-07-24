class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countT = {}
        countS = {}
        for letter in range(len(s)):
            countT[t[letter]] = countT.get(t[letter], 0) + 1
            countS[s[letter]] = countS.get(s[letter], 0) + 1
        return countT == countS