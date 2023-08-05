def solution(nums):
    ans = [0] * len(nums)
    postfix = 1
    for i in range(len(nums)):
        ans[i] = postfix
        postfix *= nums[i]
    prefix = 1
    for i in range(len(nums) - 1, -1, -1):
        ans[i] *= prefix
        prefix *= nums[i]
    return ans

print(solution([1,2,3,4]))
        