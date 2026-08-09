# works on adjacent swaps

from typing import List


class Solution:
    def bubble_sort(self, arr:List[int]) -> List[int]:
        for i in range(len(arr), 0, -1): # 
            is_swapped = False
            for j in range(len(arr) - 1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    is_swapped = True
            if not is_swapped:
                return arr
        return arr

s = Solution()
arr = [5, 8, 1, 6, 9, 2, 3, 4, 7]
arr = [1,2,3,4,5,6,7,8,9]
print(s.bubble_sort(arr))

# length is 9 means we have to sort 9 times, but we can optimize it by checking if any swaps were made in the inner loop. If no swaps were made, the array is already sorted and we can break early.
# i = 9, j = 0, 1, 2, 3, 4, 5, 6, 7, 8
# Time complexity: O(n^2) in worst case, O(n) in best case (when the array is already sorted)
# Space complexity: O(1) because we are sorting in place and not using any extra space.