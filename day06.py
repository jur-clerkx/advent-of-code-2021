from functools import cache


def parse_input(lines):
    fishes = []
    for line in lines:
        for x in line.strip().split(','):
            fishes.append(int(x))

    return fishes

@cache
def fish_count(days, fish):
    count = 1
    while days > 0:
        days -= fish
        fish = 7
        if days > 0:
            count += fish_count(days, 9)
    return count


def part_1(lines):
    fishes = parse_input(lines)
    return sum(fish_count(80, fish) for fish in fishes)


def part_2(lines):
    fishes = parse_input(lines)
    return sum(fish_count(256, fish) for fish in fishes)


if __name__ == '__main__':
    input_file = open('input/day06.txt', 'r')
    lines = input_file.readlines()
    print(part_1(lines))
    print(part_2(lines))
