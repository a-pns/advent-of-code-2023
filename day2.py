from utilities import get_inputs_from_file


class GameSimulator:
    def __init__(self, arg_red, arg_green, arg_blue):
        self.limits = {}
        self.limits["red"] = arg_red
        self.limits["green"] = arg_green
        self.limits["blue"] = arg_blue

    def calculate_games(self, arg_array_of_games):
        sum = 0
        for line in arg_array_of_games:
            sum += self._process_game(line)
        return sum

    def calculate_power_games(self, arg_array_of_games):
        sum = 0
        for line in arg_array_of_games:
            sum += self._process_power_game(line)
        return sum

    def _process_power_game(self, arg_game_string):
        if arg_game_string == "" or arg_game_string is None:
            raise RuntimeError("Invalid Game Line - Empty or None")
        _, cubes = self._split_game(arg_game_string)
        power = 1
        for key in cubes:
            power = power * cubes[key]
        return power

    def _process_game(self, arg_game_string):
        if arg_game_string == "" or arg_game_string is None:
            raise RuntimeError("Invalid Game Line - Empty or None")
        id, cubes = self._split_game(arg_game_string)
        for key in cubes.keys():
            if self.limits[key] < cubes[key]:
                return 0
        return id

    def _split_game(self, arg_game_string):
        game, round_strings = arg_game_string.split(":")
        print(f"'{game}'", f"'{round_strings}'")
        _, game_id = game.split(" ")
        rounds = self._split_game_into_rounds(round_strings)
        cubes = {}
        for round in rounds:
            new_cubes = self._split_game_round(round)
            for nc_keys in new_cubes:
                if cubes.get(nc_keys):
                    cubes[nc_keys] = max(cubes[nc_keys], new_cubes[nc_keys])
                else:
                    cubes[nc_keys] = new_cubes[nc_keys]
        return int(game_id), cubes

    def _split_game_into_rounds(self, arg_game_rounds):
        return arg_game_rounds.split(";")

    def _split_game_round(self, arg_round_string):
        return_matrix = {}
        results = arg_round_string.strip().split(",")
        for result in results:
            num, colour = result.strip().split(" ")
            return_matrix[colour] = int(num)
        return return_matrix


def process_game_from_file(arg_game, arg_file_path):
    return arg_game.calculate_games(get_inputs_from_file(arg_file_path))


def process_power_game_from_file(arg_game, arg_file_path):
    return arg_game.calculate_power_games(get_inputs_from_file(arg_file_path))
