def f(arr: list[str]) -> list[str]:
    """
    Time:  O(n)
    Space: O(n)
    """
    moves = {
        "R": lambda pos: (pos[0] + 1, pos[1]),
        "D": lambda pos: (pos[0], pos[1] - 1),
        "L": lambda pos: (pos[0] - 1, pos[1]),
        "U": lambda pos: (pos[0], pos[1] + 1),
    }

    i = 0
    pos = (0, 0)
    vector = [pos]
    visited = set([pos])
    result = []
    while i < len(arr):
        move = arr[i]
        pos = moves[move](pos)

        if pos in visited:
            while vector and pos != vector[-1]:
                visited.remove(vector[-1])
                vector.pop()
                result.pop()
        else:
            visited.add(pos)
            vector.append(pos)
            result.append(move)

        i += 1

    return result


assert f(["R", "D", "L", "U"]) == []
assert f(["R", "D", "L", "U", "R"]) == ["R"]
assert f(["R", "D", "L", "R", "U", "U", "R"]) == ["R", "U", "R"]
assert f(["R", "D", "D", "L", "L", "R", "R", "U", "U"]) == ["R"]
assert f(
    ["R", "D", "D", "L", "U", "L", "D", "D", "R", "R", "R", "U", "U", "U", "L"]
) == ["R"]
