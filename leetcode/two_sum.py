"""Two sum question."""
# https://leetcode.com/problems/two-sum/description/
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.

# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # output_index_list = []
    # # Convert to tuples with indices
    # nums_tuples = []
    # for idx, num in enumerate(nums):
    #     nums_tuples.append((num, idx))

    # if target >= 0:
    #     nums_tuples.sort(key=lambda tup: tup[0])
    # else:
    #     nums_tuples.sort(key=lambda tup: tup[0], reverse=True)
    # while nums_tuples:
    #     current_num_tuple = nums_tuples.pop()

    #     if target >= 0:
    #         if current_num_tuple[0] <= target:
    #             target -= current_num_tuple[0]
    #             output_index_list.insert(0, current_num_tuple[1])
    #     elif target < 0:
    #         if current_num_tuple[0] < 0 and current_num_tuple[0] >= target:
    #             target -= current_num_tuple[0]
    #             output_index_list.insert(0, current_num_tuple[1])
    #     # elif target == 0:
    #     #     if current_num_tuple[0] == 0:
    #     #         output_index_list.insert(0, current_num_tuple[1])

    # return output_index_list

    # This works, but is inefficient:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return sorted([i, j])

# Test cases
print two_sum(nums=[2, 7, 11, 15], target=9)

print two_sum(nums=[3, 2, 3], target=6)

print two_sum(nums=[3, 2, 4], target=6)

print two_sum(nums=[-1, -2, -3, -4, -5], target=-8)

print two_sum(nums=[0], target=-8)

print two_sum(nums=[0, 4, 3, 0], target=0)

print two_sum(nums=[-3, 4, 3, 90], target=0)
