class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        count_s1 = Counter(s1) 
        count_window = {}
        for right in range(len(s2)):
            count_window[s2[right]] = count_window.get(s2[right], 0) + 1
            if right - left + 1  > len(s1):
                count_window[s2[left]]-=1
                if count_window[s2[left]] == 0:
                    del count_window[s2[left]]
                left+=1
            if (right - left + 1) == len(s1):
                if count_window == count_s1:
                    return True
        return False 


                 
