from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0

        for i, i_height in enumerate(height):
            left = right = 0

            for j, j_height in enumerate(height):

                if j < i:
                    left = max(left, j_height)
                elif j > i:
                    right = max(right, j_height)

            contrib = min(left, right) - i_height

            if contrib > 0:
                area += contrib

        return area