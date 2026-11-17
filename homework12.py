def counting_sort(arr):
    if len(arr) == 0:
        return []
    k = max(arr)
    count = [0] * (k + 1)
    for x in arr:
        count[x] += 1
    result = []
    for v in range(k + 1):
        result += [v] * count[v]
    return result

data = [4, 2, 2, 8, 3, 3, 1, 0, 4, 0]
print("Відсортований масив:", counting_sort(data))
