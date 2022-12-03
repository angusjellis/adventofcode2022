class Items:
    def get_priority(self, item:str):
        if item >= "a" and item <= "z":
            priority = ord(item) - ord("a") + 1
        else:
            priority = ord(item) - ord("A") + 27
        return priority

    def sum_priorities(self):
        priority_sum = sum(self.get_priority(item) for item in self.common_items)
        return priority_sum

class Rucksack(Items):
    def __init__(self, items: str):
        halfway = int(len(items) / 2)
        self.first_compartment = set(items[0:halfway])
        self.second_compartment = set(items[halfway:])

    def get_common_items(self):
        common_items = self.first_compartment.intersection(self.second_compartment)
        self.common_items = common_items

class ElfGroup(Items):
    def __init__(self, input:zip):
        self.first_elf = set(input[0])
        self.second_elf = set(input[1])
        self.third_elf = set(input[2])

    def get_common_items(self):
        common_items = self.first_elf.intersection(self.second_elf, self.third_elf)
        self.common_items = common_items


with open("input.txt", "r") as input_file:
    summed_priorities_rucksacks = 0
    items_string = input_file.read().splitlines()
    for i in items_string:
        sack = Rucksack(i)
        sack.get_common_items()
        summed_priorities_rucksacks += sack.sum_priorities()

    print(summed_priorities_rucksacks)

    summed_priorities_elves = 0
    for z in (zip(*[iter(items_string)] * 3)):
        group = ElfGroup(z)
        group.get_common_items()
        summed_priorities_elves += group.sum_priorities()
    
    print(summed_priorities_elves)
