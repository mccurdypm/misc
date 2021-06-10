
#Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
#If target exists, then return its index. Otherwise, return -1.

def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            midpoint = left + (right - left) //2
            print 'midpoint: {}'.format(midpoint)
            print nums[midpoint]
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                left = midpoint + 1
            else:
                right = midpoint - 1
        return midpoint
