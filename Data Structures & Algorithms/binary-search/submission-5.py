class Solution:
    def search(self, nums: List[int], target: int) -> int:
        inicio = 0
        fim = len(nums) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if nums[meio] == target:
                return meio
            elif nums[meio] < target:
                inicio = meio + 1
            else:
                fim = meio - 1
        return -1
