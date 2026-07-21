class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        verified_nums = set()
        for i in nums:
            if i in verified_nums:
                return True
            verified_nums.add(i)
        return False
            
        