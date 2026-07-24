class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        items = set()
        for num in nums:
            if num not in items:
               items.add(num)

            else:
                return True
       
        return False