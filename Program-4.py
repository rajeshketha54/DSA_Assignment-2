# In an array, Count Pairs with given sum
def count_pairs_with_sum(arr, target_sum):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                count += 1
    return count
arr = [1,2,3,4,5]
target_sum = 6
pair_count = count_pairs_with_sum(arr, target_sum)
print("Number of pairs with the sum", target_sum, ":", pair_count)
    
