#Container with most water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
       
        left = 0
        right = len(height) - 1
        max_water = 0

#------------beats 97% run time  --------------------
        while left < right:
            height_left = height[left]
            height_right = height[right]
            width = right - left
        
            if height_right > height_left:
                area = height[left] * width
                left += 1
            
            else:
                area = height[right] * width 
                right -= 1
            
            if max_water < area:
                max_water = area
        return max_water

# ----------------- This logic bets 12% in runtime ---------------------
        # while left < right:
        #     width = right - left 
        #     current_water =  min(height[left], height[right]) * width
        #     max_water = max(max_water, current_water)

        #     if height[right] < height[left]:
                
        #         right -= 1
        #     else:
        #         left += 1
        # return max_water