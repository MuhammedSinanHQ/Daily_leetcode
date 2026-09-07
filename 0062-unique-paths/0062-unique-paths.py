import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # We need to make a total of (m - 1) + (n - 1) moves.
        # We just need to choose (m - 1) down moves from the total moves.
        return math.comb(m + n - 2, m - 1)