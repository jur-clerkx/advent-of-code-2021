from functools import partial
from enum import Enum


def process_forward(state, amount):
    h, v = state
    h += amount
    return h, v


def process_up(state, amount):
    h, v = state
    v -= amount
    return h, v


def process_down(state, amount):
    h, v = state
    v += amount
    return h, v


class InputEnum(Enum):
    forward = partial(process_forward)
    up = partial(process_up)
    down = partial(process_down)

    def __call__(self, *args):
        return self.value(*args)


def process_forward2(state, amount):
    h, v, aim = state
    h += amount
    v += amount * aim
    return h, v, aim


def process_up2(state, amount):
    h, v, aim = state
    aim -= amount
    return h, v, aim


def process_down2(state, amount):
    h, v, aim = state
    aim += amount
    return h, v, aim


class InputEnum2(Enum):
    forward = partial(process_forward2)
    up = partial(process_up2)
    down = partial(process_down2)

    def __call__(self, *args):
        return self.value(*args)


if __name__ == '__main__':
    input_file = open('input/day02.txt', 'r')
    h_state, v_state = 0, 0
    input_lines = [line.split(' ') for line in input_file.readlines()]
    for command, amount in input_lines:
        h_state, v_state = InputEnum[command]((h_state, v_state), int(amount))

    print("Horizontal state: {}".format(h_state))
    print("Vertical state: {}".format(v_state))
    print("Multiplied state: {}".format(h_state * v_state))

    h_state, v_state, aim_state = 0, 0, 0
    for command, amount in input_lines:
        h_state, v_state, aim_state = InputEnum2[command]((h_state, v_state, aim_state), int(amount))

    print("Part 2 ------------")
    print("Horizontal state: {}".format(h_state))
    print("Vertical state: {}".format(v_state))
    print("Multiplied state: {}".format(h_state * v_state))

