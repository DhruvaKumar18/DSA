#27 Remove Element
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        k=0
        for i in range(len(nums)):   #iterate through the array
            if nums[i] != val:       #check if the current element is not equal to val
                nums[k] = nums[i]    #place the element at index k
                k+=1
        return k