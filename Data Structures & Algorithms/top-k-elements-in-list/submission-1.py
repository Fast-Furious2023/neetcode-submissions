class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       # count = Counter(nums)
       # return sorted(count, key = lambda x : -count[x])[:k]

       #count
       count = {}
       for n in nums:
        count[n] = count.get(n,0) + 1

       #bucket sort
       frequency = [[] for _ in range(len(nums)+1)]
       for num, cnt in count.items():
        frequency[cnt].append(num)

       #get top k result
       result = []
       for i in range(len(nums), 0, -1):
        for element in frequency[i]:
            result.append(element)
            if len(result) == k:
                return result
