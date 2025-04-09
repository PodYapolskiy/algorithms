class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        Time:  O(n)
        Space: O(1)
        """
        start, end = 0, len(numbers) - 1

        while start < end:
            summary = numbers[start] + numbers[end]
            if summary == target:
                return [start + 1, end + 1]
            if summary > target:
                end -= 1
            else:
                start += 1

        return [-1, -1]
