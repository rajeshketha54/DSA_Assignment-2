# Find the Kth largest and Kth smallest number in an array

def find_kth_largest_smallest(arr, k):
    sorted_arr = sorted(arr)
    k_smallest = sorted_arr[k - 1]
    k_largest = sorted_arr[-k]
    return k_smallest, k_largest
array = [9, 4, 2, 7, 1, 5, 8, 3, 6]
k = 3
k_smallest, k_largest = find_kth_largest_smallest(array, k)
print(f"The {k}th smallest number is {k_smallest}")
print(f"The {k}th largest number is {k_largest}")
