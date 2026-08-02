class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        if k == 1:
            return -nums[0]
        
        for i in range(0,k-1):
            heapq.heappop(nums)
        
        return -nums[0]