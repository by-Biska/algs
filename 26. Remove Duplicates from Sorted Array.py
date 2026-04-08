from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_cursor = 1
        for i in range(len(nums)):
            if nums[i] != nums[i-1]:
                nums[write_cursor] = nums[i-1]
                write_cursor += 1
        return write_cursor

nums = [1,1,2]
sol = Solution()
print(sol.removeDuplicates(nums))
