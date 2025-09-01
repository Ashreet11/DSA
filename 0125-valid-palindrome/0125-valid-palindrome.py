class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers at the start and end of the string
        left = 0
        right = len(s) - 1
      
        # Continue checking while the pointers haven't crossed
        while left < right:
            # Skip non-alphanumeric character on the left
            if not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric character on the right
            elif not s[right].isalnum():
                right -= 1
            # Check if characters don't match (case-insensitive)
            elif s[left].lower() != s[right].lower():
                return False
            # Characters match, move both pointers inward
            else:
                left += 1
                right -= 1
      
        # All characters matched successfully
        return True