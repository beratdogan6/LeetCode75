class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        my_array = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    my_array[i] *= nums[j]
        
        return my_array