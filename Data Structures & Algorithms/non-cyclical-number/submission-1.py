class Solution:
    def isHappy(self, n: int) -> bool:
        vistos = set() 
        while n != 1:
            if n in vistos:
                return False
            vistos.add(n)
            total_sum = 0
            for digit in str(n):
                total_sum += int(digit) * int(digit)
            n = total_sum
        return True