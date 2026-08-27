class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        indexes = []
        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                indexes.append(i)
                indexes.append(seen[complement])
                return sorted(indexes)
            else:
                seen[n] = i