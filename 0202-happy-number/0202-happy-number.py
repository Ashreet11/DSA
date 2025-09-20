class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(n):
            total = 0 
            while n > 0:
                digit = n % 10
                total += digit * digit 
                n //= 10
            return total 

        slow = n
        fast = n 
        while True:
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))

            if slow == 1 or fast == 1:
                return True 
            if slow == fast:
                return False




          

