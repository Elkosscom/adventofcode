with open("input", "r") as f:
    wires = []
    for line in f:
        wires.append(line[:-1].split(","))


def trace_wire(wire: list) -> list:
    output = [(0, 0)]
    for step in wire:
        length = int(step[1:])
        direction = step[0]
        if direction == "U":
            for i in range(1, length + 1):
                last = output[len(output) - 1]
                output.append((last[0], last[1] + 1))
        elif direction == "D":
            for i in range(1, length + 1):
                last = output[len(output) - 1]
                output.append((last[0], last[1] - 1))
        elif direction == "L":
            for i in range(1, length + 1):
                last = output[len(output) - 1]
                output.append((last[0] - 1, last[1]))
        elif direction == "R":
            for i in range(1, length + 1):
                last = output[len(output) - 1]
                output.append((last[0] + 1, last[1]))
    return output


wire1 = trace_wire(wires[0])
wire2 = trace_wire(wires[1])

intersections = set(wire1) & set(wire2)
manhattan_distances = [abs(t[0]) + abs(t[1]) for t in intersections]
part_1 = manhattan_distances[:]
part_1.sort()
print(f"Part 1: {part_1[1]}")

steps = []
for i in intersections:
    a = wire1.index(i)
    b = wire2.index(i)
    steps.append((a, b))
part_2 = [abs(t[0]) + abs(t[1]) for t in steps]
part_2.sort()
print(f"Part 2: {part_2[1]}")
