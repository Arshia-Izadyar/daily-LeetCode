def solution(strs):
    hashT = {}
    for i in strs:
        sorted_str = "".join(sorted(i))
        if sorted_str in hashT:
            hashT[sorted_str].append(i)
        else:
            hashT[sorted_str] = [i]
    return hashT.values()
    
    

from collections import defaultdict

def solution2(strs):
    hash_map = defaultdict(list)
    for s in strs:
        count= [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        hash_map[tuple(count)].append(s)
    return hash_map.values()
        
print(solution2(["eat","tea","tan","ate","nat","bat"]))

