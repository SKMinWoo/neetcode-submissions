class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for key, val in count.items():
            freq[val].append(key)

        results = []
        for val in range(len(freq) -1, 0, -1):
            for i in freq[val]:
                results.append(i)
                if len(results) == k:
                    return results