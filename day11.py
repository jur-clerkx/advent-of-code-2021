def string_array_to_int_array(line):
    return list(map(int, line))


def parse_input(lines):
    result = [list(line.strip()) for line in lines]
    return list(map(string_array_to_int_array, result))


def get_adjacent_points(x, y):
    possible_points = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y + 1), (x - 1, y - 1), (x + 1, y - 1),
                       (x + 1, y + 1)]
    return list(filter(lambda vector: 0 <= vector[0] <= 9 and 0 <= vector[1] <= 9, possible_points))


def increase_value(x, y, data, flashed):
    data[y][x] = data[y][x] + 1
    if data[y][x] > 9:
        process_flash(x, y, data, flashed)


def process_flash(x, y, data, flashed):
    if (x, y) not in flashed:
        flashed.add((x, y))
        for point_x, point_y in get_adjacent_points(x, y):
            increase_value(point_x, point_y, data, flashed)


def do_step(data):
    flashed = set()
    for y in range(10):
        for x in range(10):
            increase_value(x, y, data, flashed)
    for x, y in flashed:
        data[y][x] = 0
    return len(flashed)


def part_1(lines):
    data = parse_input(lines)
    count = 0
    for step in range(100):
        count += do_step(data)
    return count


def part_2(lines):
    data = parse_input(lines)
    step = 0
    while True:
        step += 1
        if do_step(data) == 100:
            break
    return step


if __name__ == '__main__':
    input_file = open('input/day11.txt', 'r')
    lines = input_file.readlines()
    print(part_1(lines))
    print(part_2(lines))
