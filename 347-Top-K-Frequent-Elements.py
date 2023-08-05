def topKFrequent(nums, k):
    count = {}
    freq = [[] for _ in range(len(nums))]
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)
    ans = []
    for i in range(len(freq) -1 ,0, -1):
        for n in freq[i]:
            ans.append(n)
        if len(ans) == k:
            return ans
        
        