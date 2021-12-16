def parse_input(lines):
    return [list(line.strip()) for line in lines]


def get_adjacent_points(x, y, max_x, max_y):
    points = []
    if x != 0:
        points.append((x - 1, y))
    if x != max_x:
        points.append((x + 1, y))
    if y != 0:
        points.append((x, y - 1))
    if y != max_y:
        points.append((x, y + 1))
    return points


def is_low_point(x, y, max_x, max_y, data):
    value = int(data[y][x])
    adjacent_points = get_adjacent_points(x, y, max_x, max_y)
    for point_x, point_y in adjacent_points:
        if value >= int(data[point_y][point_x]):
            return False
    return True


def get_bassin(x, y, max_x, max_y, data, checked_points):
    count = 0
    if int(data[y][x]) != 9:
        checked_points.add((x, y))
        count += 1
        next_points = set(get_adjacent_points(x, y, max_x, max_y)) - checked_points
        for point_x, point_y in next_points:
            checked_points = get_bassin(point_x, point_y, max_x, max_y, data, checked_points)
    return checked_points


def part_1(lines):
    data = parse_input(lines)
    max_y = len(data) - 1
    max_x = len(data[0]) - 1
    count = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if is_low_point(x, y, max_x, max_y, data):
                count += int(data[y][x]) + 1
    return count


def part_2(lines):
    data = parse_input(lines)
    max_y = len(data) - 1
    max_x = len(data[0]) - 1
    bassins = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if is_low_point(x, y, max_x, max_y, data):
                bassins.append(len(get_bassin(x, y, max_x, max_y, data, set())))
    bassins.sort(reverse=True)
    return bassins[0] * bassins[1] * bassins[2]


if __name__ == '__main__':
    input_file = open('input/day09.txt', 'r')
    lines = input_file.readlines()
    print(part_1(lines))
    print(part_2(lines))
