class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Time:  O(n)
        Space: O(n)
        """
        forms = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
        forms_keys = list(sorted(forms.keys(), reverse=True))
        sub_forms = {900: "CM", 400: "CD", 90: "XC", 40: "XL", 9: "IX", 4: "IV"}
        sub_forms_keys = list(sorted(sub_forms.keys(), reverse=True))

        arr = []
        n = 1000
        while num:
            d = num // n
            if d == 0:
                n //= 10
                continue

            maxi = None
            cur_list = sub_forms_keys if d == 4 or d == 9 else forms_keys
            for number in cur_list:
                if number <= d * n:
                    maxi = number
                    break

            num -= maxi
            value = sub_forms[maxi] if d == 4 or d == 9 else forms[maxi]
            arr.append(value)

        return "".join(arr)
