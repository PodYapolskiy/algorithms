class Solution:
    def compress(self, chars: list[str]) -> int:
        """
        Time:  O(n)
        Space: O(1)
        """
        i, n = 0, len(chars)

        while i < n:
            # count current token
            count = 0
            token = chars[i]
            while i < n and chars[i] == token:
                count += 1
                i += 1

            # append to the end counted result
            chars.append(token)
            if count > 1:  # if more than one add number as separate digits
                temp = []
                while count:
                    temp.append(str(count % 10))
                    count //= 10
                chars.extend(temp[::-1])

        chars[:] = chars[i:]  # reassign with no copy
        return len(chars)
