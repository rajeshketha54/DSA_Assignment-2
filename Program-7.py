#Move all the negative elements to one side of the array

def move_negative_elements(array):
    return [x for x in array if x < 0] + [x for x in array if x >= 0]

array = [1, 2, 3, 4, 5, 6, -5, -4, -3, -8]
modified = move_negative_elements(array)
print(modified)
