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
    array_length = len(nums)
    sub_array_sum = 0
    if k == 1:
        return max(nums)
    for subarray_length in range(1, k + 1):
        for ind in range(array_length - subarray_length + 1):
            current_subarray_sum = sum(nums[ind : ind + subarray_length])
            if current_subarray_sum > sub_array_sum:
                sub_array_sum = current_subarray_sum
    return sub_array_sum
