from statistics import median


def parse_input(lines):
    crabs = []
    for line in lines:
        for x in line.strip().split(','):
            crabs.append(int(x))

    return crabs


def calculate_fuel_cost(position, crabs):
    total = 0
    for crab in crabs:
        cost = crab - position
        if cost < 0:
            cost *= -1
        total += cost
    return total


def calculate_fuel_cost_new(position, crabs):
    total = 0
    for crab in crabs:
        steps = crab - position
        if steps < 0:
            steps *= -1
        total += sum(range(steps + 1))
    return total


def part_1(lines):
    crabs = parse_input(lines)
    ideal_position = round(median(crabs))
    return calculate_fuel_cost(ideal_position, crabs)


def part_2(lines):
    crabs = parse_input(lines)
    ideal_position = int(sum(crabs) / len(crabs))
    return min(calculate_fuel_cost_new(ideal_position, crabs), calculate_fuel_cost_new(ideal_position + 1, crabs))


if __name__ == '__main__':
    input_file = open('input/day07.txt', 'r')
    lines = input_file.readlines()
    print(part_1(lines))
    print(part_2(lines))
