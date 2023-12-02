from utilities import get_inputs_from_file


def evaluate_line(arg_line):
    if len(arg_line) == 0:
        raise RuntimeError("Line is empty")
    digits = []
    for char in arg_line:
        if char.isdigit():
            digits.append(char)
    if len(digits) == 0:
        raise RuntimeError(f"There were no digits found: {arg_line}")
    return int(digits[0] + digits[-1])


def _convert_spelt_line_to_digit_line(arg_line):
    digit_mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    new_string = ""
    process_string = ""
    for char in arg_line:
        process_string += char
        if char.isdigit():
            new_string += char
            process_string = ""
        else:
            for key in digit_mapping.keys():
                if key in process_string:
                    new_string += digit_mapping[key]
                    process_string = ""
    return new_string


def evaluate_multiple_lines(arg_array_lines):
    evaluation = 0
    for line in arg_array_lines:
        evaluation += evaluate_line(line)
    return evaluation


def evaluate_multiple_spelt_lines(arg_array_lines):
    evaluation = 0
    for line in arg_array_lines:
        new_line = _convert_spelt_line_to_digit_line(line)
        evaluation += evaluate_line(new_line)
    return evaluation


def evaluate_day1_scenario(arg_file_input):
    return evaluate_multiple_lines(get_inputs_from_file(arg_file_input))


def evaluate_day1_b_scenario(arg_file_input):
    return evaluate_multiple_spelt_lines(get_inputs_from_file(arg_file_input))
