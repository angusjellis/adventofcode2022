# Challenge One:
# find all the pairs where one pair fully contains the other


class ElfPair:
    def __init__(self, input: str):

        self.elves = [[int(e) for e in i.split("-")] for i in input.split(",")]
        self.elf_ranges = [range((elf[0] - 1), (elf[1] + 1)) for elf in self.elves]

    def pair_unoptimal(self):
        elf_one_range = self.elf_ranges[0]
        elf_two_range = self.elf_ranges[1]
        return (
            elf_one_range.start in elf_two_range and elf_one_range[-1] in elf_two_range
        ) or (
            elf_two_range.start in elf_one_range and elf_two_range[-1] in elf_one_range
        )

    def pair_very_unoptimal(self):
        elf_one_range = self.elf_ranges[0]
        elf_two_range = self.elf_ranges[1]
        return max(elf_one_range.start, elf_two_range.start) < min(
            elf_one_range[-1], elf_two_range[-1]
        )


with open("input.txt", "r") as input_file:
    unoptimal_pairings = 0
    very_unoptimal_pairings = 0
    items_string = input_file.read().splitlines()
    for i in items_string:
        e = ElfPair(i)
        if e.pair_unoptimal():
            unoptimal_pairings += 1
        if e.pair_very_unoptimal():
            very_unoptimal_pairings += 1


print(unoptimal_pairings)
print(very_unoptimal_pairings)
