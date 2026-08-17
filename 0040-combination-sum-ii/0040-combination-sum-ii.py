class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort to easily skip duplicates and prune the search space early
        candidates.sort()
        result = []
        
        def backtrack(start_index, current_combo, current_sum):
            # Base case: we found a valid combination
            if current_sum == target:
                result.append(list(current_combo))
                return
            
            # Base case: we exceeded the target, no need to continue this path
            if current_sum > target:
                return
            
            # Explore further combinations
            for i in range(start_index, len(candidates)):
                # Skip duplicate elements at the same depth level
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                
                # Choose the current candidate
                current_combo.append(candidates[i])
                
                # Explore with the chosen candidate 
                # Note: pass i + 1 because we can't reuse the same element
                backtrack(i + 1, current_combo, current_sum + candidates[i])
                
                # Backtrack: remove the candidate to try the next one
                current_combo.pop()
                
        backtrack(0, [], 0)
        return result