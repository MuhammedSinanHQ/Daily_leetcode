class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        target = len(nums) - 1
        
        for i, jump in enumerate(nums):
            # If the current index is beyond our maximum reach, we're stuck.
            if i > max_reach:
                return False
                
            # Update the maximum reach we can achieve from this index.
            max_reach = max(max_reach, i + jump)
            
            # If our reach meets or exceeds the last index, we can finish.
            if max_reach >= target:
                return True
                
        return False