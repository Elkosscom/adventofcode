with open("input", "rb") as f:
    content = f.read().decode("utf8")


def validate(num: int) -> bool:
    digits = [int(d) for d in str(num)]

    adjacent = [True for i in range(5) if digits[i] == digits[i + 1]]

    increasing = []
    for i in range(5):
        if digits[i] <= digits[i + 1]:
            increasing.append(True)
        else:
            increasing.append(False)
    sequences = [digits.count(c) for c in set(digits)]  # PART 2

    if len(digits) != 6:
        return False
    elif not adjacent:
        return False
    elif False in increasing:
        return False
    elif 2 not in sequences:  # PART 2
        return False
    else:
        return True


ran = (content[0:6], content[7:-1])
passwords = []


for i in range(int(ran[0]), int(ran[1]) + 1):
    if validate(i):
        passwords.append(i)

print(len(passwords))

