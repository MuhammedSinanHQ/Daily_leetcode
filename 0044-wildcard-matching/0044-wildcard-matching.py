class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_idx = 0
        p_idx = 0
        star_idx = -1
        s_tmp_idx = -1
        
        while s_idx < len(s):
            # Case 1: Characters match or pattern has '?'
            if p_idx < len(p) and (p[p_idx] == '?' or p[p_idx] == s[s_idx]):
                s_idx += 1
                p_idx += 1
            
            # Case 2: Pattern has '*', record its position and the current string position
            elif p_idx < len(p) and p[p_idx] == '*':
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1 # Assume '*' matches zero characters initially
                
            # Case 3: Mismatch, but we've seen a '*' previously. Backtrack and use '*' to match more characters.
            elif star_idx != -1:
                p_idx = star_idx + 1
                s_tmp_idx += 1
                s_idx = s_tmp_idx
                
            # Case 4: Mismatch and no '*' seen previously
            else:
                return False
                
        # Check if the remaining characters in the pattern are all '*'
        while p_idx < len(p) and p[p_idx] == '*':
            p_idx += 1
            
        return p_idx == len(p)