

def is_exist(lsts: list[list[int]], num: int) -> bool:
    count = 0
    for lst in lsts:
        for l in lst:
            if l == num:
                count += 1
    return (len(lsts) == count)

def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    arr = []
    for lst in lists:
        if not lst:
            return ([])

        new_arr = set(lst)
        arr.append(list(new_arr))

    res_arr = []
    for lst in arr:
        for el in lst:
            if is_exist(arr, el) and el not in res_arr:
                res_arr.append(el)
    return res_arr

res = [
    (list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]), [2, 3]),
    (list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]), [4]),
    (list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]]), [1, 2, 3]),
    (list_intersection_finder([[1, 2, 3], [4, 5, 6]]), []),
    (list_intersection_finder([]), []),
    (list_intersection_finder([[1, 2, 3], []]), []),
    (list_intersection_finder([[5]]), [5])
]

try:
    for r, a in res:
        print(r == a)
except Exception as e:
    print(e)