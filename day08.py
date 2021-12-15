def parse_input(lines):
    return [(line.split(' | ')[0].strip().split(), line.split(' | ')[1].strip().split()) for line in lines]


def part_1(lines):
    data = parse_input(lines)
    return sum(len(list(filter(lambda x: len(x) in [2, 4, 3, 7], output))) for _, output in data)


def part_2(lines):
    return None


if __name__ == '__main__':
    input_file = open('input/day08.txt', 'r')
    lines = input_file.readlines()
    print(part_1(lines))
    print(part_2(lines))
