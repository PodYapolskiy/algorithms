class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        # to handle last range add denitely larger with step 2
        nums.append(nums[-1] + 2)

        start = 0  # index of start of cur range
        answer = []
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                rng = f"{nums[start]}->{nums[i]}" if i + 1 - start > 1 else f"{nums[i]}"
                answer.append(rng)
                start = i + 1

        return answer
