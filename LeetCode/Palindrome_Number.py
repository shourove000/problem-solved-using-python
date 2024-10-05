class Solution:
    def isPalindrome(self, x: int) -> bool:
        # y = [int(digit) for digit in str(x)] 
        x = list(str(x))
        print(x)
        reversed_x = x[::-1]  
        print(reversed_x)
        return x == reversed_x
