class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visitados = set()
        def backtrack(estado):
            if len(nums) == len(estado):
                res.append(list(estado))
                return
            for num in nums:
                if num not in visitados:
                    visitados.add(num)
                    estado.append(num)
                    backtrack(estado)
                    visitados.remove(num)
                    estado.pop()
        backtrack([])
        return res


