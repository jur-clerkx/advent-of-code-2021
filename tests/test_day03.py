from day03 import get_most_common_bits, get_most_common_bit, get_least_common_bit, get_oxygen_bit_string, \
    get_co2_bit_string


def test_calculate_most_common_bits():
    all_ones = ['11111', '11111', '11111']
    assert get_most_common_bits(all_ones) == '11111'

    all_zeros = ['00000', '00000', '00000']
    assert get_most_common_bits(all_zeros) == '00000'

    easy_test = ['11111', '11111', '00000', '00000', '11111']
    assert get_most_common_bits(easy_test) == '11111'

    hard_test = ['111010000101', '001001110011', '101001101111', '101110101110', '101000101111']
    assert get_most_common_bits(hard_test) == '101000101111'


def test_most_common_bit():
    test_data = ['1', '1', '0']
    assert get_most_common_bit(test_data) == '1'
    test_data = ['1', '1', '1']
    assert get_most_common_bit(test_data) == '1'
    test_data = ['0', '1', '1']
    assert get_most_common_bit(test_data) == '1'
    test_data = ['0', '1', '0']
    assert get_most_common_bit(test_data) == '0'
    test_data = ['0', '0', '0']
    assert get_most_common_bit(test_data) == '0'
    test_data = ['1', '0', '0']
    assert get_most_common_bit(test_data) == '0'
    test_data = ['1', '0', '0', '1']
    assert get_most_common_bit(test_data) == '1'
    test_data = ['0', '0', '1', '1']
    assert get_most_common_bit(test_data) == '1'


def test_least_common_bit():
    test_data = ['1', '1', '0']
    assert get_least_common_bit(test_data) == '0'
    test_data = ['1', '1', '1']
    assert get_least_common_bit(test_data) == '0'
    test_data = ['0', '1', '1']
    assert get_least_common_bit(test_data) == '0'
    test_data = ['0', '1', '0']
    assert get_least_common_bit(test_data) == '1'
    test_data = ['0', '0', '0']
    assert get_least_common_bit(test_data) == '1'
    test_data = ['1', '0', '0']
    assert get_least_common_bit(test_data) == '1'
    test_data = ['1', '0', '0', '1']
    assert get_least_common_bit(test_data) == '0'
    test_data = ['0', '0', '1', '1']
    assert get_least_common_bit(test_data) == '0'


def test_get_oxygen_bit_string():
    test_data = ['11111', '11111', '00000', '00000', '11111']
    assert get_oxygen_bit_string(test_data) == '11111'
    test_data = ['10111', '11011', '00000', '00100', '11100']
    assert get_oxygen_bit_string(test_data) == '11100'


def test_get_c02_bit_string():
    test_data = ['11111', '11111', '00000', '00000', '11111']
    assert get_co2_bit_string(test_data) == '00000'
    test_data = ['10111', '11011', '00000', '01100', '11100']
    assert get_co2_bit_string(test_data) == '00000'
