class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        window_sum = 0
        res = 0 
        for r in range(len(arr)):
            window_sum += arr[r]
            if r - l + 1 == k:
                if window_sum >= threshold * k:
                    res +=1
                window_sum -=arr[l]
                l+=1
        return res