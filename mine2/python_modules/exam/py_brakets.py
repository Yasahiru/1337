

def valid(s: str) -> bool:
    open = ['(', '[', '{']
    close = [')', '}', ']']
    lst = []

    i = 0
    while (i < len(s)):
        if s[i] in open:
            lst.append(s[i])
        elif s[i] in close:
            if not lst:
                return False
            t = lst.pop()
            if s[i] == ')' and t != '(':
                return False
            if s[i] == ']' and t != '[':
                return False
            if s[i] == '}' and t != '{':
                return False
        i += 1
    return (len(lst) == 0)
