class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]

        for i in nums:
            count[i] += 1

        i = 0
        for n in range(len(count)):
            for k in range(count[n]):
                nums[i] = n
                i += 1
        