#26. Remove Duplicates from Sorted Array
class Solution(object):
    
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:  #Check for empty list
            return 0

        k = 1
<<<<<<< HEAD
        for i in range(1,len(nums)):  #Start from second element
=======
        for i in range(1,len(nums)):  
>>>>>>> 0f622e64bedc2702ef02e569679f778b302dcd08
            if nums[i] != nums[i-1]:  #compare current element with previous one
                nums[k] = nums[i]     #place unique element at index k
                k += 1
        return k