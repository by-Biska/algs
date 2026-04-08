from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]

        right_prod = 1
        print(result)
        for i in range(n-1, -1, -1):
            result[i] *= right_prod

            right_prod *= nums[i]
        return result
sol = Solution()
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))