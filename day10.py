from collections import deque
from statistics import median

CORRUPT_SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

COMPLETE_SCORES = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

VALID_PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def parse_input(lines):
    return [list(line.strip()) for line in lines]


def get_corrupted_line_score(line):
    chunks = deque()
    for char in line:
        if char in VALID_PAIRS:
            # New chunk opened
            chunks.append(char)
        else:
            # Not an opening statement, correct closing expected
            expected = VALID_PAIRS.get(chunks.pop())
            if expected != char:
                return CORRUPT_SCORES[char]
    return 0


def calculate_autocomplete_score(chunks):
    score = 0
    while chunks:
        score *= 5
        score += COMPLETE_SCORES.get(chunks.pop())
    return score


def get_autocomplete_line_score(line):
    chunks = deque()
    for char in line:
        if char in VALID_PAIRS:  # Valid line, so if not opening statement then it's a valid closing statement
            chunks.append(char)
        else:
            chunks.pop()
    return calculate_autocomplete_score(chunks)


def part_1(lines):
    data = parse_input(lines)
    count = 0
    for line in data:
        count += get_corrupted_line_score(line)
    return count


def part_2(lines):
    data = parse_input(lines)
    scores = []
    for line in data:
        if get_corrupted_line_score(line) == 0:
            scores.append(get_autocomplete_line_score(line))
    return median(scores)


if __name__ == '__main__':
    input_file = open('input/day10.txt', 'r')
    lines = input_file.readlines()
    print(part_1(lines))
    print(part_2(lines))
