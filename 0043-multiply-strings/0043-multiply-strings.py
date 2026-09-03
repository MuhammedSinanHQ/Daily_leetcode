class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case: if either number is zero, the product is zero
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        # The maximum possible length of the product is m + n
        res = [0] * (m + n)
        
        # Iterate from right to left over both strings
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Multiply the current digits
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                
                # Positions in the result array
                p1, p2 = i + j, i + j + 1
                
                # Add the multiplication to the existing value at p2
                total = mul + res[p2]
                
                # Update the result array
                res[p2] = total % 10
                res[p1] += total // 10
                
        # Convert the integer array to a string
        result_str = "".join(map(str, res))
        
        # Strip any leading zeros and return
        return result_str.lstrip("0")