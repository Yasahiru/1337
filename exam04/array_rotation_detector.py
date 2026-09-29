

def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if not arr1 or not arr2:
        return True
    if len(arr1) != len(arr2):
        return False

    new_arr = arr1
    arrays = []

    i = 0
    while i < len(arr1):
        el = new_arr.pop()
        new_arr.insert(0, el)
        arrays.append(new_arr.copy())
        i += 1

    if arr2 not in arrays:
        return False
    return True




res = [
    (array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]), True),
    (array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]), True),
    (array_rotation_detector([1, 2, 3], [3, 2, 1]), False),
    (array_rotation_detector([1, 2], [1, 2, 3]), False),
    (array_rotation_detector([], []), True)
]

for r, a in res:
    print(r == a)
