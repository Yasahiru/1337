

def sort_lst(lst: list[int]) -> list[int]:
    checker = 1
    while (checker):
        checker = 0
        for i in range(len(lst) - 1):
            if lst[i + 1] < lst[i]:
                tmp = lst[i + 1]
                lst[i + 1] = lst[i]
                lst[i] = tmp
                checker = 1
    return lst


def place_number(lst: list[int], num: int) -> None:
    new_arr = lst
    c = 0
    for n in lst:
        if n > num:
            new_arr.insert(c, num)
            break
        else:
            new_arr.append(num)
            break
        c += 1
    lst = new_arr.copy()
    return lst


def merge_two_lsts(lst1: list[int], lst2: list[int]) -> list[int]:
    res = []
    for l in lst2:
        res = place_number(lst1, l)
    return res


def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    for lst in lists:
        sort_lst(lst)

    i = 1
    size = len(lists)
    new_arr = []
    while (i < size - 1):
        for lst in lists[i]:
            res = merge_two_lsts(list[i], list[i + 1])
            print(list[i], list[i + 1])
            new_arr.extend(res)
        i += 1
    return lists[0]

# print(merge_sorted_lists([[1, 3, 5], [2, 4, 6]]))
print(merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]]))

# res = merge_two_lsts([1, 2, 3], [4, 5, 6])
# print(res)