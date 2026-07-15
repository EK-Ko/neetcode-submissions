class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # step 1: binary search the first elements of the rows
        # step 2: binary search the elements from the target row

        up, down = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        index = 0

        while up <= down:
            index = up + (down-up) // 2
            if matrix[index][0] == target:
                return True
            elif matrix[index][0] < target:
                up = index + 1
            else:
                down = index - 1
        
        index = down

        while left <= right and index >= 0:
            horMid = left + (right-left) //2
            if matrix[index][horMid] < target:
                left = horMid + 1
            elif matrix[index][horMid] > target:
                right = horMid - 1
            else:
                return True

        return False
