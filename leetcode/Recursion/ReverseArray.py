from typing import List
def reverseArray(nums: List, left, right)->List:
    if (left >= right or left > right):
        return nums
    nums[left], nums[right] = nums[right], nums[left]
    return reverseArray(nums, left +1, right - 1)


print(reverseArray(nums = [5,7,3,2,6,1,5,9], left = 0, right=7))

