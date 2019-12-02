## PART 1
def calculate_fuel(mass):
    return mass // 3 - 2


assert calculate_fuel(12) == 2
assert calculate_fuel(14) == 2
assert calculate_fuel(1969) == 654
assert calculate_fuel(100756) == 33583


with open(r"input", "r") as f:
    modules = [int(line[0:-1]) for line in f.readlines()]

total = 0
for module in modules:
    total += calculate_fuel(module)

print(f"Part 1:{total}")


## Part 2
def calculate_total_fuel(mass: int) -> int:
    output = 0
    temp = mass
    while True:

        temp = calculate_fuel(temp)
        if temp <= 0:
            break
        output += temp
        temp = temp
    return output


assert calculate_total_fuel(1969) == 966
assert calculate_total_fuel(100756) == 50346


total_fuel = 0
for mass in modules:
    total_fuel += calculate_total_fuel(mass)


print(f"Part 2: {total_fuel}")

