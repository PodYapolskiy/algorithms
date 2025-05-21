def index_pairs(s: str) -> int:
    mem: dict[str, int] = {}
    left = result = 0

    for right in range(len(s)):
        if s[right] in mem:
            left = mem[s[right]] + 1

        mem[s[right]] = right
        result += right - left + 1

    return result


assert index_pairs("") == 0
assert index_pairs("a") == 1
assert index_pairs("aba") == 5  # (0, 0), (1, 1), (2, 2), (0, 1), (1, 2)
assert index_pairs("abcab") == 12
