from itertools import permutations


with open(r"input", "r") as f:
    intcode = [int(i) for i in f.read().split(",")]


def gravity_assist(input_list, noun, verb):
    code = input_list[:]
    code[1] = noun
    code[2] = verb

    x = 0
    while x < len(code):
        if code[x] == 99:
            break
        elif code[x] == 1:
            code[code[x + 3]] = code[code[x + 1]] + code[code[x + 2]]
            x += 4
        elif code[x] == 2:
            code[code[x + 3]] = code[code[x + 1]] * code[code[x + 2]]
            x += 4
        else:
            print("Something went wrong!")
            break
    return code[0]


print(f"Part 1: {gravity_assist(intcode,12,2)}")

for pair in permutations(range(100), 2):
    noun, verb = pair
    if gravity_assist(intcode, noun, verb) == 19690720:
        print(f"Part 2: {100*noun+verb}")
