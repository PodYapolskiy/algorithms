from rich import print


class Solution:
    def firstUniqChar(self, string: str) -> int:
        mem, max_index = {}, len(string)
        for index, letter in enumerate(string):
            # if first occurence, current index
            # if second, max index to indicate later
            mem[letter] = index if letter not in mem else max_index
        return (
            min(mem.values())  # minimum index if any does not equel to amx
            if any(value != max_index for value in mem.values())
            else -1
        )


print(Solution().firstUniqChar("leetcode"))  # 0
print(Solution().firstUniqChar("loveleetcode"))  # 2
print(Solution().firstUniqChar("aabb"))  # -1
