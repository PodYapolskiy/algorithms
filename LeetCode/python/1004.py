class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_len = start = end = 0

        while end < len(nums):
            # expand stage (to right)
            while k >= 0 and end < len(nums):
                if nums[end] == 0:
                    k -= 1
                if k >= 0:  # important check not to shift when k < 0 achived
                    end += 1
            max_len = max(max_len, end - start)  # do not include end

            # shrink stage (from left)
            while k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1

            # when shrink enough shift from last 0 to the right
            end += 1

        return max_len
