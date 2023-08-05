def Twosum(nums,t):
    hash_map = {}
    for i, v in enumerate(nums):
        comp = t - v
        if comp in hash_map:
            return [i, hash_map[comp]]
        else:
            hash_map[v] = i
    
print(Twosum([3,3], 6))