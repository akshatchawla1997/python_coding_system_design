class Solution:
    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_index = i
            for j in range( i+ 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

s = Solution()
arr = [64, 25, 12, 22, 11]
print(s.selection_sort(arr))