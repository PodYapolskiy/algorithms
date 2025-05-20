class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Time:  O(n)
        Space: O(1)
        """
        prev = None
        cur_ptr = swp_ptr = cur_cnt = 0

        while cur_ptr < len(nums):
            if nums[cur_ptr] != prev:
                cur_cnt = 0
                prev = nums[cur_ptr]

            cur_cnt += 1
            if cur_cnt > 2:
                # shift until next non-duplicate
                while cur_ptr < len(nums) and nums[cur_ptr] == prev:
                    cur_ptr += 1
                # assign new prev and cur if not end
                if cur_ptr < len(nums):
                    cur_cnt = 1
                    prev = nums[cur_ptr]

            # if not reached end continue swaping current pointer and swap pointer
            if cur_ptr < len(nums):
                nums[cur_ptr], nums[swp_ptr] = nums[swp_ptr], nums[cur_ptr]
                cur_ptr += 1
                swp_ptr += 1

        return swp_ptr


nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(Solution().removeDuplicates(nums))
print(nums)
