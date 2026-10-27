# From Day 16 onwards, you will be creating your own PyCharm projects from scratch.
# Instead of using templates that I have created for you.
# It will be another step in your journey as a developer!
# But don't worry, I will explain how to do everything in the video tutorials on Udemy.
nums = [1, 2, 1, 1, 3]

new_nums = []

for num in nums:
    if num not in new_nums:
        new_nums.append(num)
print(len(new_nums))