from collections import deque


def create_instruction(instruction: str) -> tuple:
    i = instruction[5:]
    first_space = i.index(" ")
    num_moves = int(i[:first_space])
    i = i[first_space + 6 :]
    first_space = i.index(" ")
    from_stack = int(i[:first_space])
    to_stack = int(i[first_space + 4 :])
    return num_moves, from_stack, to_stack


class CrateMover:
    def __init__(self, stacks: list):
        stacks.reverse()
        initial_stacks_object = {}
        for s in stacks:
            real_index = -1
            for l in s:
                real_index += 1
                if l.isdigit():
                    initial_stacks_object[s.index(l)] = [l]

                elif s.index(l) % 4 == 1 and l != " ":
                    initial_stacks_object[real_index].append(l)

        self.stacks_object = {}
        for s, v in initial_stacks_object.items():
            num = int(v[0])
            self.stacks_object[num] = v

    def get_top_objects(self) -> str:
        top_objects_string = ""
        for i in self.stacks_object.values():
            top_objects_string += i[-1]
        return top_objects_string


class CrateMover9000(CrateMover):
    def __init__(self, stacks: list):
        super().__init__(stacks)

    def move(self, num_moves: int, from_stack: int, to_stack: int):
        for i in range(num_moves):
            self.stacks_object[to_stack].append(
                self.stacks_object[from_stack].pop()[-1]
            )


class CrateMover9001(CrateMover):
    def __init__(self, stacks: list):
        super().__init__(stacks)

    def move(self, num_moves: int, from_stack: int, to_stack: int):
        chunk = self.stacks_object[from_stack][-num_moves:]
        self.stacks_object[to_stack].extend(chunk)
        self.stacks_object[from_stack] = self.stacks_object[from_stack][:-num_moves]


with open("./day5/input.txt", "r") as input_file:
    stacks, instructions = input_file.read().split("\n\n")

    stack_list = stacks.splitlines()

    # crate_mover_9000 = CrateMover9000(stack_list)

    crate_mover_9001 = CrateMover9001(stack_list)

    for i in instructions.splitlines():
        num_moves, from_stack, to_stack = create_instruction(i)
        # crate_mover_9000.move(num_moves, from_stack, to_stack)
        crate_mover_9001.move(num_moves, from_stack, to_stack)

    # print(crate_mover_9000.get_top_objects())
    print(crate_mover_9001.get_top_objects())
