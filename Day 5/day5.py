with open("input", "r") as f:
    code = f.read().split(",")


def get_value(param, mode):
    if mode == "0":
        return int(code[int(param)])
    elif mode == "1":
        return int(param)
    else:
        raise ValueError


def intcode_array(array: list):  # TODO
    array[0] = "00000"[: len(array[0]) - 1] + array[0]


pos = 0
while pos < len(code):  # TODO
    if True:
        pass
    else:
        break
# opcode 1 adds params
# opcode 2 multiplies params
# opcode 99 breaks
