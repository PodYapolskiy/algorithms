class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Time:  O(n)
        Space: O(n)
        """
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        w2l, l2w = {}, {}
        for letter, word in list(zip(pattern, words)):
            w, l = l2w.get(letter, None), w2l.get(word, None)

            # if any is present tha check for inconsistences
            if (w or l) and (word != w or letter != l):
                return False

            # update dicts reprenting bijection
            w2l[word] = letter
            l2w[letter] = word

        return True
