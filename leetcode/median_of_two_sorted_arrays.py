from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Edge cases for when either array is empty
        if not nums1:
            return self.medianList(nums2)
        elif not nums2:
            return self.medianList(nums1)

        nums1Index = nums2Index = 0

        total_length = len(nums1) + len(nums2)

        # The position of the median in the merged array
        medianIndex = total_length / 2 - 0.5

        # This is the index we reach once we have PASSED the median index
        midpoint_limit = medianIndex + 0.5 if total_length % 2 == 0 else medianIndex

        # Current element and previous store values for just visited number and one before
        current_element = min(nums1[nums1Index], nums2[nums2Index])
        previous_element = current_element

        while True:
            # Index in merged array
            k = nums1Index + nums2Index

            if k <= midpoint_limit:
                # Havent got through to past median element yet...
                previous_element = current_element

                # Checked for if the first array has been exhausted
                if nums1Index == len(nums1):
                    # Reached end of first array
                    current_element = nums2[nums2Index]
                    nums2Index += 1
                    continue

                # Check for if the second array has been exhausted or
                if nums2Index == len(nums2):
                    current_element = nums1[nums1Index]
                    nums1Index += 1
                    continue

                # Whether we want to put the element from 1st or 2nd array in current_element
                # i.e. finding next element in merged array
                if nums1[nums1Index] < nums2[nums2Index]:
                    # i.e. the value at nums1Index would come first
                    current_element = nums1[nums1Index]
                    nums1Index += 1
                else:
                    current_element = nums2[nums2Index]
                    nums2Index += 1

            else:
                break

        return current_element if total_length % 2 != 0 else (current_element + previous_element) / 2

    def medianList(self, nums: List[int]) -> float:
        # Method to return the median of a List
        length = len(nums)

        if length % 2 == 0:
            # even length
            return 0.5 * (nums[length // 2 - 1] + nums[length // 2])
        else:
            return nums[length // 2]