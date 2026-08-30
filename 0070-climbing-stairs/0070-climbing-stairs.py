class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: if n is 1 or 2, the number of ways is n itself
        if n <= 2:
            return n
        
        # We only need to store the results of the previous two steps
        prev1, prev2 = 1, 2
        
        # Calculate for step 3 up to n
        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
            
        return prev2