def ranges(arr: list[int]) -> list[str]:
    if not arr:
        return []

    minima, maxima, counter = min(arr), max(arr), 0
    mem = set(arr)
    answer = []

    for n in range(minima, maxima + 1 + 1):  # second + 1 handles last elem
        if n in mem:
            counter += 1
        elif counter > 0:
            rng = f"{n - 1}" if counter == 1 else f"{n - counter}-{n - 1}"
            answer.append(rng)
            counter = 0

    return answer


assert ranges([1, 2, 3, 5, 6, 7, 11]) == ['1-3', '5-7', '11']
assert ranges([5, 1, 7, 6, 3, 11, 2]) == ['1-3', '5-7', '11']
assert ranges([]) == []
assert ranges([1]) == ["1"]
