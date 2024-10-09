class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the Roman numeral values and their corresponding symbols
        roman_values = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ]
        
        result = ""
        
        # Loop through the values and symbols
        for value, symbol in roman_values:
            if num == 0:
                break
            count = num // value  # Find out how many times the symbol fits
            result += symbol * count  # Add the symbol count times to the result
            num %= value  # Reduce the number by the value
        
        return result

# Example usage
solution = Solution()
print(solution.intToRoman(1987))  # Output: "MCMLXXXVII"
