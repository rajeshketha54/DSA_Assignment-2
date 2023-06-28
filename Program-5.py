#Find duplicates in an array
def find_duplicates(arr):
    duplicates = []
    numbers = set()

    for num in arr:
        if num in numbers:
            duplicates.append(num)
        else:
            numbers.add(num)
    return duplicates
array = [1,2,3,4,5,5,2,1]
duplicates = find_duplicates(array)
print("Duplicate numbers :",duplicates)
    
