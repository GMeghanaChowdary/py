def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Input
n = int(input())
arr = list(map(int, input().split()))

# Sort the list using Insertion Sort
insertion_sort(arr)

# Output
print(" ".join(map(str, arr)))
