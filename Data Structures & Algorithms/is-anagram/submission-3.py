class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        words = dict()
        if len(s) != len(t):
            return False
        for letter in s:
            words[letter] = words.get(letter, 0) + 1
        for letter in t:
            words[letter] = words.get(letter, 0) - 1 
        return all(value == 0 for value in words.values())

