def calculate_fuel(mass):
    return int(mass / 3) - 2


assert calculate_fuel(12) == 2
assert calculate_fuel(14) == 2
assert calculate_fuel(1969) == 654
assert calculate_fuel(100756) == 33583


with open("1_input.txt", "r") as f:
    modules = [line[0:-1] for line in f.readlines()]

print(modules)
total = 0
for module in modules:
    print(calculate_fuel(int(module)))
    total += calculate_fuel(int(module))

print(f"Total:{total}")
