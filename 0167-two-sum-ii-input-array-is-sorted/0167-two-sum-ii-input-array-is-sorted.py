class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right: 
            currsum = numbers[left] + numbers[right]

            if currsum == target:
                return [left+1, right+1] # +1 because LeetCode requires 1-based indexing

            elif currsum < target:
                left += 1

            else: 
                right -= 1
        
        return None

"""
LeetCode 167: Two Sum II - Input Array is Sorted
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Approach: Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)
"""
"""
DRY RUN
numbers = [2, 7, 11, 15], target = 9

left=0 (2), right=3 (15) → sum=17 > 9 → right--
left=0 (2), right=2 (11) → sum=13 > 9 → right--
left=0 (2), right=1 (7) → sum=9 == target ✅ return [1, 2]

"""