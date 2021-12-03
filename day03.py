def get_most_common_bit(bit_array):
    return max(['1', '0'], key=bit_array.count)


def get_least_common_bit(bit_array):
    return min(['0', '1'], key=bit_array.count)


def bit_strings_to_bit_arrays(bit_strings):
    bit_strings = [bit_string.strip() for bit_string in bit_strings]
    bit_arrays = []
    for bit_string in bit_strings:
        if not bit_arrays:
            for bit in bit_string:
                bit_arrays.append([bit])
        else:
            counter = 0
            for bit in bit_string:
                bit_arrays[counter].append(bit)
                counter += 1
    return bit_arrays


def get_most_common_bits(bit_strings):
    bit_arrays = bit_strings_to_bit_arrays(bit_strings)
    result = ''
    for bit_array in bit_arrays:
        result += get_most_common_bit(bit_array)
    return result


def get_oxygen_bit_string(bit_strings):
    count = 0
    result_array = bit_strings
    while len(set(result_array)) > 1:
        bit_arrays = bit_strings_to_bit_arrays(result_array)
        most_common_bit = get_most_common_bit(bit_arrays[count])
        result_array = list(filter(lambda bit_string: bit_string[count] == most_common_bit, result_array))
        count += 1
    return result_array[0]


def get_co2_bit_string(bit_strings):
    count = 0
    result_array = bit_strings
    while len(set(result_array)) > 1:
        bit_arrays = bit_strings_to_bit_arrays(result_array)
        least_common_bit = get_least_common_bit(bit_arrays[count])
        result_array = list(filter(lambda bit_string: bit_string[count] == least_common_bit, result_array))
        count += 1
    return result_array[0]


def invert_bit_string(bit_string):
    return ''.join('1' if x == '0' else '0' for x in bit_string)


if __name__ == '__main__':
    input_file = open('input/day03.txt', 'r')
    input_lines = input_file.readlines()
    most_common_bits = get_most_common_bits(input_lines)
    least_common_bits = invert_bit_string(most_common_bits)
    print("Most common bits {}".format(most_common_bits))
    print("Most least bits {}".format(least_common_bits))
    print("Multiplied {}".format(int(most_common_bits, 2) * int(least_common_bits, 2)))
    oxygen_bits = get_oxygen_bit_string(input_lines)
    co2_bits = get_co2_bit_string(input_lines)
    print("Oxygen bits {}".format(oxygen_bits))
    print("CO2 bits {}".format(co2_bits))
    print("Multiplied {}".format(int(oxygen_bits, 2) * int(co2_bits, 2)))
