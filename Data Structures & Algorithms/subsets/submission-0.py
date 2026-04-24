class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, estado):
            res.append(list(estado))            
            for i in range(start, len(nums)):
                estado.append(nums[i])
                backtrack(i + 1, estado)
                estado.pop()
        backtrack(0, [])
        return res
                