import collections


def parse_input(lines):
    line_vectors = []
    for line in lines:
        vectors = line.strip().split(' -> ')
        start_vector = (int(vectors[0].split(',')[0]), int(vectors[0].split(',')[1]))
        end_vector = (int(vectors[1].split(',')[0]), int(vectors[1].split(',')[1]))
        line_vectors.append((start_vector, end_vector))
    return line_vectors


def get_line_horizontal_vertical_point_vectors(line_vector):
    start_vector, end_vector = line_vector
    start_x, start_y = start_vector
    end_x, end_y = end_vector
    result = []
    if start_x == end_x:
        while start_y != end_y:
            result.append((start_x, start_y))
            if start_y < end_y:
                start_y += 1
            else:
                start_y -= 1
        result.append((start_x, start_y))
    elif start_y == end_y:
        while start_x != end_x:
            result.append((start_x, start_y))
            if start_x < end_x:
                start_x += 1
            else:
                start_x -= 1
        result.append((start_x, start_y))
    return result


def get_offset(start, end):
    if start == end:
        return 0
    elif start > end:
        return -1
    else:
        return 1


def get_all_line_point_vectors(line_vector):
    start_vector, end_vector = line_vector
    start_x, start_y = start_vector
    end_x, end_y = end_vector
    result = []
    while start_x != end_x or start_y != end_y:
        result.append((start_x, start_y))
        start_x += get_offset(start_x, end_x)
        start_y += get_offset(start_y, end_y)
    result.append((start_x, start_y))
    return result


def get_overlapping_points(point_vectors):
    point_count = collections.Counter(point_vectors)
    i = 0
    for _, count in point_count.items():
        if count >= 2:
            i += 1
    return i


def part_1(lines):
    line_vectors = parse_input(lines)
    point_vectors = list(sum(map(get_line_horizontal_vertical_point_vectors, line_vectors), []))
    return get_overlapping_points(point_vectors)


def part_2(lines):
    line_vectors = parse_input(lines)
    point_vectors = list(sum(map(get_all_line_point_vectors, line_vectors), []))
    return get_overlapping_points(point_vectors)


if __name__ == '__main__':
    input_file = open('input/day05.txt', 'r')
    lines = input_file.readlines()
    print(part_1(lines))
    print(part_2(lines))
