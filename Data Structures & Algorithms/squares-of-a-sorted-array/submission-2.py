class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        l = 0
        r = len(nums) -1
        idx = -1
        while l <= r:
            l_sq = nums[l] * nums[l]
            r_sq = nums[r] * nums[r]
            if l_sq > r_sq:
                res[idx] = l_sq
                l+=1
            else:
                res[idx] = r_sq
                r-=1
            idx-=1
        return res
 









#class Solution:
#    def sortedSquares(self, nums: List[int]) -> List[int]:
#        res = []
 #       l,r = 0, len(nums) - 1
 #       while l <= r:
 #           if nums[l] * nums[l] > nums[r] * nums[r]:
 #               res.append(nums[l] * nums[l])
 #               l += 1
 #           else:
 #               res.append(nums[r] * nums[r])
 #               r -= 1
 #       return res[::-1]

               