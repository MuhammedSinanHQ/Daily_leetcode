class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        # Loop until both strings are exhausted and there's no carry left
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            
            # Append the current bit (carry modulo 2)
            res.append(str(carry % 2))
            
            # Update the carry for the next position (carry divided by 2)
            carry //= 2
            
        # The result is built backwards, so reverse it and join to a string
        return "".join(res[::-1])