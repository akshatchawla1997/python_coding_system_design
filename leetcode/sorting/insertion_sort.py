class Sorting:
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):

            for j in range(i):
                if arr[i] < arr[j]:
                    key = arr[i]
                    while j < i:
                        arr[j + 1] = arr[j]
                        j += 1
                    arr[j] = key
        return arr

s = Sorting()
arr = [12, 11, 13, 5, 6]
print(s.insertion_sort(arr))  # Output: [5, 6, 11, 12, 13]