# KADANE'S ALGORITHM TO FIND MAXIMUM SUBARRAY IN ARRAY

# Given an integer array nums, we find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

def maxSubArray(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums)==1:
        return nums[0]
    if all(x<0 for x in nums):
        return max(nums)
    max_ending_here = 0
    max_so_far = 0
    global start
    global end
    s = 0
    for i in range(0,len(nums)):
        max_ending_here += nums[i]
        if max_ending_here<0:
            s = i+1
            max_ending_here = 0
        if max_so_far<max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
    return max_so_far

# Main
nums = [-2,1,-3,4,-1,2,1,-5,4]
start = 0 # Start Index of Maximum Subarray
end = 0 # End Index of Maximum Subarray
print("Maximum Sum =",maxSubArray(nums)) # 6 because [4,-1,2,1] has the largest sum = 6.
print("Start Index of Maximum Subarray =",start) # 3
print("End Index of Maximum Subarray =",end) # 6
print("Maximum Subarray =",nums[start:end+1]) # [4,-1,2,1]