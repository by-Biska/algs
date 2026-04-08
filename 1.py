from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
      prefixSum =[0] * len(nums)
      prefixSum[0] = nums[0]
      for i in range(1, len(nums)):
        prefixSum[i] = prefixSum[i-1] + nums[i]
      prefixSumRemainder = [x % k for x in prefixSum]
      return prefixSumRemainder
      
sol = Solution()
nums = [23,2,6,4,7]
k = 6
print(sol.checkSubarraySum(nums, k))