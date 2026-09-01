class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # Initialize a DP table with dimensions (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases: converting to/from an empty string
        for i in range(m + 1):
            dp[i][0] = i  # i deletions
        for j in range(n + 1):
            dp[0][j] = j  # j insertions
            
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If the characters match, no new operation is needed
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # If they don't match, take the minimum of Insert, Delete, or Replace
                else:
                    dp[i][j] = min(
                        dp[i][j - 1] + 1,    # Insert
                        dp[i - 1][j] + 1,    # Delete
                        dp[i - 1][j - 1] + 1 # Replace
                    )
                    
        # The answer is in the bottom-right corner
        return dp[m][n]