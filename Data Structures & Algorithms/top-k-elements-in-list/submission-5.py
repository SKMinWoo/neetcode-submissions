class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] = count.get(i, 0) + 1

        for key, val in count.items():
            freq[val].append(key)

        results = []
        for vals in range(len(freq) -1, 0, -1):
            for i in freq[vals]:
                results.append(i)
                if len(results) == k:
                    return results