def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

# Input
n = int(input())
arr = list(map(int, input().split()))

# Sort the list using Selection Sort
selection_sort(arr)

# Output
print(" ".join(map(str, arr)))
