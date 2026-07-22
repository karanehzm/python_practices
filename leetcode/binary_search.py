class Solution:
    def search(self, nums: list[int], target: int) -> int:

        start = 0
        end = len(nums)-1
        mid = (start + end ) // 2
        
        for _ in nums:
            if target == nums[mid]:
                return mid

            elif target < nums[mid]:
                
                end = mid 
                mid = (start + end ) //2

            elif target > nums[mid]:
                start = mid
                end = len(nums)
                mid = (start + end) // 2

        return -1

                




        