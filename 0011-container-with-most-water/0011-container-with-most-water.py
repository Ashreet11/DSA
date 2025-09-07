class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0 
        left, right = 0, len(height)-1
        while left < right:
            area = (right-left) * min(height[left], height[right])
            res = max(res, area)

            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                left += 1 # this is for when the heights are same so we can do either  left+=1 or right -= 1 doesnt matter(basically move either of the pointers doesnt matter)
        return res