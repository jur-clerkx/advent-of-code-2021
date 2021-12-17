from collections import Counter
from functools import cache


def parse_input(lines):
    template_line = lines[0].strip()
    rules = dict(line.strip().split(' -> ') for line in lines if ' -> ' in line)
    return template_line, rules


def process_rules(line, steps):
    line_pairs = list(zip(line, line[1:]))
    counter = Counter(list(line))
    for pair in line_pairs:
        counter += process_pair(pair, steps)
    return counter


@cache
def process_pair(pair, steps):
    string_pair = pair[0] + pair[1]
    if string_pair in rules:
        rule = rules[string_pair]
        result = Counter([rule])
        if steps == 1:
            return result
        else:
            return result + process_pair((pair[0], rule), steps - 1) + process_pair((rule, pair[1]), steps - 1)
    else:
        return Counter()


def part_1(lines):
    template_line, rules = parse_input(lines)
    counter = process_rules(template_line, 10)
    return counter.most_common()[0][1] - counter.most_common()[-1][1]


def part_2(lines):
    template_line, rules = parse_input(lines)
    counter = process_rules(template_line, 40)
    return counter.most_common()[0][1] - counter.most_common()[-1][1]


if __name__ == '__main__':
    input_file = open('input/day14.txt', 'r')
    lines = input_file.readlines()
    _, rules = parse_input(lines)
    print(part_1(lines))
    print(part_2(lines))
