def solution(nums):
    longest = 0
    numset = set(nums)
    for  n in nums:
        if n - 1 not in numset:
            length = 0
            while (length + n) in numset:
                length += 1
            longest = max(length, longest)
    return longest

print(solution([0,3,7,2,5,8,4,6,0,1]))