from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # sort so duplicates are adjacent
        used = [False] * len(nums)
        res = []
        path = []

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # skip duplicates:
                # if current equals previous and previous wasn't used in this branch,
                # using nums[i] now would create duplicate permutation
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack()

                path.pop()
                used[i] = False

        backtrack()
        return res