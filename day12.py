from collections import Counter, defaultdict
import cProfile


def parse_input(lines):
    edges = [line.strip().split('-') for line in lines]
    result = defaultdict(list)
    for edge in edges:
        node1, node2 = edge
        if node2 != 'start':
            result[node1].append(node2)
        if node1 != 'start':
            result[node2].append(node1)
    return result


def get_options(current, data):
    current_loc = current[-1]
    return data.get(current_loc, [])


def is_path_valid(path):
    counter = Counter(path)
    for key, value in counter.items():
        if key.islower() and value > 1:
            return False
    return True


def is_path_valid2(path):
    counter = Counter(path)
    visited_small_caves_twice = 0
    for key, value in counter.items():
        if key.islower() and value > 1:
            visited_small_caves_twice += value
    if visited_small_caves_twice > 2:
        return False
    return True


def get_paths(current):
    if current[-1] == 'end':
        return [current]
    paths = []
    for option in get_options(current, data):
        path = [*current, option]
        if is_path_valid(path):
            paths += get_paths(path)
    return paths


def get_paths2(current):
    if current[-1] == 'end':
        return [current]
    paths = []
    for option in get_options(current, data):
        path = [*current, option]
        if is_path_valid2(path):
            paths += get_paths2(path)
    return paths


def part_1():
    return len(get_paths(['start']))


def part_2():
    return len(get_paths2(['start']))


if __name__ == '__main__':
    input_file = open('input/day12.txt', 'r')
    lines = input_file.readlines()
    data = parse_input(lines)
    print(part_1())
    print(part_2())
