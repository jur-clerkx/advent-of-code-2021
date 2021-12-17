def parse_input(lines):
    points = [(int(line.strip().split(',')[0]), int(line.strip().split(',')[1])) for line in lines if ',' in line]
    folds = [[line.strip().split('=')[0][-1], int(line.strip().split('=')[1])] for line in lines if 'fold' in line]
    return points, folds


def calculate_fold(point, fold):
    return fold - (point - fold)


def fold_x(points, fold):
    result = set()
    for x, y in points:
        if x == fold:
            continue
        if x < fold:
            result.add((x, y))
        else:
            result.add((calculate_fold(x, fold), y))
    return result


def fold_y(points, fold):
    result = set()
    for x, y in points:
        if y == fold:
            continue
        if y < fold:
            result.add((x, y))
        else:
            result.add((x, calculate_fold(y, fold)))
    return result


def part_1(lines):
    points, folds = parse_input(lines)
    first_fold = folds[0]
    if first_fold[0] == 'x':
        return len(fold_x(points, first_fold[1]))
    else:
        return len(fold_y(points, first_fold[1]))


def part_2(lines):
    points, folds = parse_input(lines)
    for fold in folds:
        if fold[0] == 'x':
            points = fold_x(points, fold[1])
        else:
            points = fold_y(points, fold[1])

    for y in range(200):
        line = ''
        for x in range(200):
            if (x, y) in points:
                line += '#'
            else:
                line += '.'
        print(line)


if __name__ == '__main__':
    input_file = open('input/day13.txt', 'r')
    lines = input_file.readlines()
    print(part_1(lines))
    part_2(lines)

# result = fold_y(points, first_fold[1])
# print(result)
# for y in range(15):
#     line = ''
#     for x in range(15):
#         if (x, y) in result:
#             line += '#'
#         else:
#             line += '.'
#     print(line)
