from typing import List


def reverse_matrix(s: List[List[int]]) -> List[List[int]]:
    i = 0
    start = 0
    end = len(s) - 1
    while (i < len(s) / 2):
        tmp = s[start]
        s[start] = s[end]
        s[end] = tmp
        i += 1
        end -= 1
        start += 1

    for lst in s:
        lst.reverse()
    return s


res = reverse_matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(res)
