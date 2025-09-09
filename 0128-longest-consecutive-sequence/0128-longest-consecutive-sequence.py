class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)   # store numbers for O(1) lookup
        longest = 0
        
        for num in s:
            # Only start counting if it's the beginning of a sequence
            if num - 1 not in s:
                next_num = num + 1
                length = 1
                
                # Expand sequence
                while next_num in s:
                    length += 1
                    next_num += 1
                
                # Update longest streak found
                longest = max(longest, length)
        
        return longest
