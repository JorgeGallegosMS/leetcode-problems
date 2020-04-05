# Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you
# have to divide it by 2, otherwise, you have to subtract 1 from it.

# 1. Restate the problem
#   Count the number of steps it takes to bring a number down to 0 by dividing by 2 if it's even and subtracting 1 when
# it's odd. Return the number of steps it takes
# 2. Ask Clarifying Questions
# 3. State Assumptions
#   The number will always be >= 0. I return the number of steps not the steps themselves.
# 4. Think Out Loud
# 4a. Brainstorm Solutions
#   Use a while loop to keep subtracting or dividing as long as the number is not 0. Increment number of steps every time
#  we subtract or divide. Once the number is 0, return the number of steps.
# 4b. Explain Your Rationale
#   We don't need any data structures, we just need to keep manipulating the number until we reach 0
# 4c. Discuss Tradeoffs
# 4d.Suggest Improvements

def numberOfSteps(num):
    steps = 0
    if num < 0:
        return f'You have entered a negative number: {num}'

    while num != 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1

        steps += 1

    return steps

print(numberOfSteps(14))