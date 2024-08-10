def bucketSort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    for num in arr:
        bi = int(n * num)
        buckets[bi].append(num)

    sorted_nums = []
    for bucket in buckets:
        sorted_nums.extend(sorted(bucket))
    return sorted_nums

arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434,0.827, 0.545, 0.356, 0.1934, 0.685, 0.3534]
print(bucketSort(arr))

