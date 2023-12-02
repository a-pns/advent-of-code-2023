def get_inputs_from_file(arg_file_input):
    line_inputs = []
    with open(arg_file_input) as file:
        next_line = file.readline()
        while next_line:
            line_inputs.append(next_line)
            next_line = file.readline()
    return line_inputs
