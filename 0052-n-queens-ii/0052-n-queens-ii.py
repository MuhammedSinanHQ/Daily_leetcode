class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        pos_diag = set()  # (row + col)
        neg_diag = set()  # (row - col)
        
        res = 0
        
        def backtrack(r):
            nonlocal res
            # If we reach row n, we have successfully placed n queens
            if r == n:
                res += 1
                return
            
            for c in range(n):
                # Check if the current square is under attack
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                # Place the queen and mark the column and diagonals as attacked
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                
                # Move to the next row
                backtrack(r + 1)
                
                # Backtrack: remove the queen to try the next column
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                
        backtrack(0)
        return res