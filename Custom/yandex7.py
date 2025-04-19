# Для заданной строки найти длину наибольшей подстроки без повторяющихся символов.
# Например:
# abcabcbbddee -> 3 (abc)
# bbbbb -> 1 (b)
# pwwkew -> 3 (wke)


def longest_substring(s: str) -> int:
    """
    Time:  O(n)
    Space: O(n)
    """
    mem = {}
    start = longest = 0

    for index, letter in enumerate(s):
        if letter in mem:
            start = mem[letter] + 1

        longest = max(longest, index - start + 1)
        mem[letter] = index

    return longest


assert longest_substring("abcabcbbddee") == 3
assert longest_substring("bbbbb") == 1
assert longest_substring("pwwkew") == 3
assert longest_substring("") == 0
assert longest_substring("a") == 1
