class Solution:
    def binary_search(self, nums, target, is_left):
        idx, start, end = -1, 0, len(nums) - 1

        while start <= end:
            mid = (end - start) // 2 + start

            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                idx = mid  # save last index of target
                if is_left:  # move to find lefter
                    end = mid - 1
                else:  # righter
                    start = mid + 1

        return idx

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        return [
            self.binary_search(nums, target, True),
            self.binary_search(nums, target, False),
        ]
