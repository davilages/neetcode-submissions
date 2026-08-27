class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        topFreq = []
        for i in range(0, k):
            top = (max(seen, key=seen.get))
            topFreq.append(top)
            del seen[top]
        return topFreq