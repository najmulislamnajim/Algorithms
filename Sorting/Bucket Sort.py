def bucketSort(nums):
        n = len(nums)
        lo, hi = min(nums), max(nums)
        
        # Edge case: if all elements are the same, return original array
        if lo == hi:
            return nums
        
        # Calculate bucket size and number of buckets
        bucket_size = max(1, (hi - lo) // (n - 1))
        bucket_count = (hi - lo) // bucket_size + 1
        
        # Initialize buckets
        buckets = [[] for _ in range(bucket_count)]
        
        # Distribute elements into buckets
        for num in nums:
            bucket_index = (num - lo) // bucket_size
            buckets[bucket_index].append(num)
        
        # Sort individual buckets and concatenate the result
        sorted_nums = []
        for bucket in buckets:
            sorted_nums.extend(sorted(bucket))
        
        return sorted_nums


nums=[408,209,142,25,193,222,796,815,864,418,605,981,760,496,197,816,62,784,399,847,44,641,381,934]

result=bucketSort(nums)
print(result)
