import os

class Elf:
    def __init__(self, number):
        self.elf_name = f"Elf {number}"
        self.food_items = []

    def add_food_item(self, item:str):
        self.food_items.append(int(item))

    def get_total_calories(self):
        total_calories = 0
        for item in self.food_items:
            total_calories += item
        return total_calories


elves = []
with open("input.txt", "r+") as input_file:
    calories_string = input_file.read()
    calories_blocks = calories_string.split("\n\n")
    formatted_blocks = [block.split("\n") for block in calories_blocks]
    i = 1
    for block in formatted_blocks:
        new_elf = Elf(i)
        for item in block:
            new_elf.add_food_item(item)
        elves.append(new_elf)
        i += 1

total_calories = []

for elf in elves:
    total_calories.append(elf.get_total_calories())

print(total_calories)

total_calories.sort(reverse=True)

top_elf_calories = total_calories[0]

top_three_elf_calories = top_elf_calories + total_calories[1] + total_calories[2]

print(top_three_elf_calories)

