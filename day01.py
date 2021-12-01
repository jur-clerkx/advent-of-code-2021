def calculate_increased_depth_counts(depths):
    current_depth = depths[0]
    count = 0
    for depth in depths[1:]:
        int_depth = depth
        if int_depth > current_depth:
            count += 1
        current_depth = int_depth
    return count


def calculate_increased_window_depths_counts(depths):
    # Build three measurements data array and use this as input for the normal method
    three_measurements_windows = []
    for depth in depths:
        # Check if it needs to be added to any existing windows
        for window in three_measurements_windows:
            if len(window) < 3:
                window.append(depth)
        # And add new window in the end
        three_measurements_windows.append([depth])
    # Calculate total value of each window and leave out non finished windows
    three_measurements_windows_values = []
    for window in three_measurements_windows:
        if len(window) == 3:
            three_measurements_windows_values.append(sum(window))
    return calculate_increased_depth_counts(three_measurements_windows_values)


if __name__ == '__main__':
    input_file = open('input/day01.txt', 'r')
    input = [int(line) for line in input_file.readlines()]
    normal_increasements = calculate_increased_depth_counts(input)
    window_increasements = calculate_increased_window_depths_counts(input)
    print('Normal increasements: {}'.format(normal_increasements))
    print('Three-measurment sliding window increasements: {}'.format(window_increasements))
