from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])

# problem is that randint is an inclusive range,
# so setting range to 1,6 gets an index out of range error