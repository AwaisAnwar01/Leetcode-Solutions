def max_subarray_sum_kadane(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage
arr = [1, -2, -6, -8, 13, 14, -16]
result = max_subarray_sum_kadane(arr)

print("Maximum Subarray Sum (Kadane's Algorithm):", result)
