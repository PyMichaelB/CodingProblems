from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seenVals = {}
        for pos, item in enumerate(nums):
            leftOver = target - item
            if leftOver in seenVals:
                # i.e. another element exists in seenVals which would add to target
                return [seenVals[leftOver], pos]
            else:
                # add item to seenVals
                seenVals[item] = pos

        return []
