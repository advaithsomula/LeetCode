class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:  # Edge case: Empty matrix
            return False

        mid1 = len(matrix) // 2  # Middle row index
        mid2 = len(matrix[mid1]) // 2  # Middle column index

        mid_element = matrix[mid1][mid2]  # Get the middle element
        
        if target == mid_element:
            return True
        
        # Search in the bottom-right quadrant
        if target > mid_element:
            for i in range(mid1, len(matrix)):  # Start from mid row
                for j in range(mid2, len(matrix[i])):  # Start from mid column
                    if matrix[i][j] == target:
                        return True
        
        # Search in the top-left quadrant
        if target < mid_element:
            for i in range(mid1, -1, -1):  # Start from mid row going up
                for j in range(mid2, -1, -1):  # Start from mid column going left
                    if matrix[i][j] == target:
                        return True
        # Search in Top-Right quadrant
        for i in range(0, mid1 + 1):  # Iterate over top rows
            for j in range(mid2 + 1, len(matrix[i])):  # Right-side columns
                if matrix[i][j] == target:
                    return True

        # Search in Bottom-Left quadrant
        for i in range(mid1 + 1, len(matrix)):  # Bottom rows
            for j in range(0, mid2):  # Left-side columns
                if matrix[i][j] == target:
                    return True
        
        return False  # If the target is not found, return False