class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            l1 = -heapq.heappop(max_heap)
            l2 = -heapq.heappop(max_heap)
            if l1 == l2:
                continue
            if l2 < l1:
                l3 = -(l1 - l2)
                heapq.heappush(max_heap, l3)

        if len(max_heap) > 0:
            return -max_heap[0]
        else:
            return 0



        