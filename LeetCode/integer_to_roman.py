class Solution:
    def intToRoman(self, num: int) -> str:
        RomanM = RomanCM =RomanD = RomanCD = RomanC= RomanXC = RomanL = RomanXL = RomanX =RomanIX = RomanV =RomanIV = RomanI = ""

        if num >= 1000:
            valueM = num // 1000
            RomanM = "M" * valueM
            num = num % 1000
        if num>=900:
            valueCM = num // 900
            RomanCM = "CM" * valueCM
            num = num % 900
        if num >= 500:
            valueD = num // 500
            RomanD = "D" * valueD
            num = num % 500
        if num >= 400:
            valueCD = num // 400
            RomanCD = "CD" * valueCD
            num = num % 400
        if num >= 100:
            valueC = num // 100
            RomanC = "C" * valueC
            num = num % 100
        if num >= 90:
            valueXC = num // 90
            RomanXC = "XC" * valueXC
            num = num % 90
        if num >= 50:
            valueL = num // 50
            RomanL = "L" * valueL
            num = num % 50
        if num >= 40:
            valueXL = num // 40
            RomanXL = "XL" * valueXL
            num = num % 40
        if num >= 10:
            valueX = num // 10
            RomanX = "X" * valueX
            num = num % 10
        if num >= 9:
            valueIX = num // 9
            RomanIX = "IX" * valueIX
            num = num % 9
        if num >= 5:
            valueV = num // 5
            RomanV = "V" * valueV
            num = num % 5
        if num >= 4:
            valueIV = num // 4
            RomanIV = "IV" * valueIV
            num = num % 4
        if num >= 1:
            valueI = num // 1
            RomanI = "I" * valueI

        # Merge and return all the Roman numeral strings
        return RomanM + RomanCM + RomanD + RomanCD + RomanC+ RomanXC + RomanL + RomanXL + RomanX +RomanIX + RomanV +RomanIV + RomanI 

# Example usage
solution = Solution()
print(solution.intToRoman(58))
