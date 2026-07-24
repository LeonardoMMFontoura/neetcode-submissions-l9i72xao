class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_of_s = {}
        for letter in s:
            if letter not in hashmap_of_s:
                hashmap_of_s[letter] = 1
            else:
                hashmap_of_s[letter] +=1
        hashmap_of_t = {}
        for letter in t:
            if letter not in hashmap_of_t:
                hashmap_of_t[letter] = 1
            else:
                hashmap_of_t[letter]+=1
        return hashmap_of_t == hashmap_of_s