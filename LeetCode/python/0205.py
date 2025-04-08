class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Time:  O(n)
        Space: O(n)
        """
        if len(s) != len(t):
            return False

        s2t, t2s = {}, {}
        for s_sym, t_sym in zip(s, t):
            if s_sym not in s2t and t_sym not in t2s:
                s2t[s_sym] = t_sym
                t2s[t_sym] = s_sym
            elif s2t.get(s_sym, None) != t_sym or t2s.get(t_sym, None) != s_sym:
                return False

        return True
