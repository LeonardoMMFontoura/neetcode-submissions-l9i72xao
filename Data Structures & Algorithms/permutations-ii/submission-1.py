class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        def permutations(path, opcoes_restantes):
            if len(path) == len(nums):
                res.append(path[:])
                return 
            visitados = set()
            for i in range(len(opcoes_restantes)):
                numero_visitado = opcoes_restantes[i] 
                if numero_visitado in visitados:
                    continue
                visitados.add(numero_visitado)
                path.append(numero_visitado)
                nova_opcao =  opcoes_restantes[:i] + opcoes_restantes[i+1:]
                permutations(path, nova_opcao)
                path.pop()
        permutations([], nums)
        return res
