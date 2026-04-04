class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Começamos com {0: 1} para o caso de cur_sum ser exatamente igual a k
        prefix_map = {0: 1}
        cur_sum = 0
        res = 0
        for n in nums:
            cur_sum += n
            diff = cur_sum - k
            # 1. Se a diferença já foi vista, somamos a FREQUÊNCIA dela ao res
            # Usamos .get(diff, 0) para não dar erro se não existir
            res += prefix_map.get(diff, 0)
            # 2. Atualizamos o caderninho: "vi esse cur_sum mais uma vez"
            prefix_map[cur_sum] = prefix_map.get(cur_sum, 0) + 1
        return res
