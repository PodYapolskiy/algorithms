def apply_stack(s, stack):
    i = 0
    while i < len(s):
        if s[i] != "#":
            stack.append(s[i])
        elif len(stack) > 0:
            stack.pop()
        i += 1


def ozon(s1: str, s2: str) -> bool:
    stack1 = []
    stack2 = []

    apply_stack(s1, stack1)
    apply_stack(s2, stack2)

    return stack1 == stack2


assert ozon("oz##on", "oz#o#n")
assert ozon("#ozon", "ozon")
assert ozon("ozon###", "oz#o#n#")
assert ozon("oz#o#n", "on")
