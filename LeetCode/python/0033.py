class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (end - start) // 2 + start

            if nums[mid] == target:  # answer itself
                return mid

            # the most diffuclt conditions
            if nums[start] <= nums[mid]:  # is start and middle follow sorting
                if nums[start] <= target <= nums[mid]:
                    end = mid  # target in correct sorting part
                else:
                    start = mid + 1  # target is further
            elif nums[mid] < nums[end]:  # another check on sorting criteria
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid

        return -1
