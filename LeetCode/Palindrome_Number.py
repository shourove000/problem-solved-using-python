class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        reversed_x = x[::-1]  
        return x == reversed_x
    
