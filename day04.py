def parse_card(lines):
    card = []
    for line in lines:
        for number in line.strip().split():
            card.append((number, False))
    return card


def parse_input(lines):
    numbers = lines[0].strip().split(',')
    lines = lines[1:]
    cards = []
    while len(lines) >= 6:
        cards.append(parse_card(lines[1:6]))
        lines = lines[6:]
    return numbers, cards


def cols(card):
    for i in range(5):
        yield [card[i + y * 5] for y in range(5)]


def rows(card):
    for i in range(5):
        yield card[i * 5: i * 5 + 5]


def has_won(card):
    return any(all(x[1] for x in col) for col in cols(card)) or any(all(x[1] for x in row) for row in rows(card))


def check_number(x, number):
    if x[0] == number:
        return x[0], True
    return x[0], x[1]


def process_number(number, cards):
    updated_cards = []
    for card in cards:
        updated_cards.append([check_number(x, number) for x in card])
    return updated_cards


def calculate_score(card, last_draw):
    unmarked_sum = 0
    for number, marked in card:
        if not marked:
            unmarked_sum += int(number)
    return int(last_draw) * unmarked_sum


def part_1(lines):
    numbers, cards = parse_input(lines)
    for number in numbers:
        cards = process_number(number, cards)
        for card in cards:
            if has_won(card):
                return calculate_score(card, number)


def part_2(lines):
    numbers, cards = parse_input(lines)
    for number in numbers:
        cards = process_number(number, cards)
        non_finished_cards = []
        for card in cards:
            if len(cards) == 1 and has_won(card):
                return calculate_score(card, number)
            if not has_won(card):
                non_finished_cards.append(card)
        cards = non_finished_cards


if __name__ == '__main__':
    input_file = open('input/day04.txt', 'r')
    lines = input_file.readlines()
    print(part_1(lines))
    print(part_2(lines))
