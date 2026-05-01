

def count(s: str):
    c = 0
    for i in s.lower():
        if i in "aeiou":
            c += 1
    return c


def crypt(tlist: list[str]) -> list[str]:
    sorted_lst = sorted(
        tlist, key=lambda s: (len(s), s.lower(), s.upper(), count(s))
    )
    return sorted_lst
