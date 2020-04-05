# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums
# [i] you have to count the number of valid j's such that j != i and nums[j] < nums[i]. Return the answer in an array

# 1. Restate the problem
#   For every number in the list count how many numbers in that same list are lower than the current number and add the
# reults to a new list. Skip if both loops are on the same index. Return the new list
# 2. Ask Clarifying Questions
#   Are the numbers sorted? Are there positive and negative numbers? What do I return if all the numbers in the list are
# the same? Ex: [7,7,7,7]
# 3. State Assumptions
#   They are not sorted. The list can have positives and negatives. I return a list of all 0s if all numbers are the same.
# Ex: [0,0,0,0]
# 4. Think Out Loud
# 4a. Brainstorm Solutions
#   Nested for loop to check the current number against all other numbers in the list
# 4b. Explain Your Rationale
#   I'm checking the same list twice so a nested for loop makes sense. I also created a list because that's what I have to
# return as the solution
# 4c. Discuss Tradeoffs
# 4d.Suggest Improvements


def smallerNumbersThanCurrent(nums):
    result = []
    length = len(nums)
    for i in range(length):
        smaller_nums = 0
        for j in range(length):
            if j != i and nums[j] < nums[i]:
                smaller_nums += 1
        result.append(smaller_nums)
        
    return result

nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))