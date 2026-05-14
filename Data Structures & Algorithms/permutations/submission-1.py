class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        def permutations(path, opcoes_restantes):
            if len(nums) == len(path):
                res.append(path[:])
                return
            for num in range(len(opcoes_restantes)): 
                numero = opcoes_restantes[num]
                path.append(numero)
                novas_opcoes = opcoes_restantes[:num] + opcoes_restantes[num+1:]
                permutations(path, novas_opcoes)
                path.pop()
        permutations([],nums)
        return res

