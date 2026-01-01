def selection_sort(arr, n):
    for i in range(n-1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]


if __name__ == "__main__":
    a = [9, 3, 1, 5, 7, 8, 4]
    n = len(a)
    selection_sort(a, n)
    print(a)
