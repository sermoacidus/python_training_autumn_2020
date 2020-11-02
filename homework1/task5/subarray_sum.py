"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if k == 1:
        return max(nums)
    sub_array_sum = 0
    for ind, elem in enumerate(nums[: -k + 1]):
        if sum(nums[ind : ind + k]) > sub_array_sum:
            sub_array_sum = sum(nums[ind : ind + k])
    return sub_array_sum
