class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        def backtrack(curr, available):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for num in list(available):
                curr.append(num)
                available.remove(num)
                backtrack(curr, available) 
                curr.pop()
                available.add(num)
        backtrack([], set(nums))
        return res 

