class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxVal = 0
        consecOnes = 0
        for i in nums:
            if (i == 1): 
                consecOnes = consecOnes + 1
                if(consecOnes > maxVal): maxVal = consecOnes       
            else: consecOnes = 0
        
        return maxVal
