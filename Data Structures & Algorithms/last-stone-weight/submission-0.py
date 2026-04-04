class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            pedra1 = -heapq.heappop(stones)
            pedra2 = -heapq.heappop(stones)
            if pedra1 == pedra2:
                continue
            elif pedra1 > pedra2:
                pedra1 -=  pedra2
                heapq.heappush(stones, -pedra1)
        return -stones[0] if len(stones) else 0


