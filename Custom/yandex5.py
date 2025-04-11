#дано две строки, например (original - «leeu» и reference «eue»)
#вернуть индекс первого вхождения reference строки в оригинальной

def f(original: str, reference: str) -> int:
    if len(original) < len(reference):
        return -1  
    if len(reference) == 0:
        return 0
    
    r = 0
    for i in range(len(original)):
        if original[i] == reference[r]:
            r += 1
        else:
            r = 0
        if r == len(reference):
            return i - r + 1
    return -1


assert f("leeu", "eue") == -1
assert f("leueue", "eue") == 1
assert f("leuueue", "eue") == 4
assert f("l", "eue") == -1
assert f("leue", "") == 0
