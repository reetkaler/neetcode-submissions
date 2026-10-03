class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False
        
        reversed_num = 0

        while x > reversed_num:
            reversed_num *= 10
            reversed_num += x % 10
            x = x // 10
        return reversed_num == x or reversed_num // 10 == x


        
        