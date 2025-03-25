class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)
        if s2_len < s1_len:
            return False

        s1_count, s2_count = {}, {}
        for i in range(s1_len):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
        if s1_count == s2_count:
            return True

        for i in range(s2_len - s1_len):
            # move window to right for 1 (delete and add last and new char)
            s2_count[s2[i + s1_len]] = s2_count.get(s2[i + s1_len], 0) + 1
            s2_count[s2[i]] -= 1

            if s2_count[s2[i]] == 0:  # if last char is no more needed erase
                del s2_count[s2[i]]

            if s1_count == s2_count:
                return True

        return False


assert Solution().checkInclusion("ab", "eidbaooo")
assert not Solution().checkInclusion("ab", "eidboaoo")
assert not Solution().checkInclusion("abc", "ab")
assert Solution().checkInclusion("abc", "abc")
assert Solution().checkInclusion("cd", "dcbabc")
assert Solution().checkInclusion("abc", "dcbabd")
assert not Solution().checkInclusion("abc", "aaab")
assert Solution().checkInclusion("adc", "dcda")
