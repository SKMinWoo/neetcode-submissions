class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        for i, n in count.items():
            buckets[n].append(i)

        results = []
        for i in range(len(buckets) -1, 0, -1):
            for val in buckets[i]:
                results.append(val)
                if len(results) == k:
                    return results