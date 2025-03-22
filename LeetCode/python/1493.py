class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        max_len = pre_cnt = cur_cnt = 0

        for n in nums:
            if n == 1:
                cur_cnt += 1
            else:
                max_len = max(max_len, pre_cnt + cur_cnt)
                pre_cnt = cur_cnt
                cur_cnt = 0

        # handle case when ends on 1
        max_len = max(max_len, pre_cnt + cur_cnt)

        return max_len if max_len < len(nums) else max_len - 1
