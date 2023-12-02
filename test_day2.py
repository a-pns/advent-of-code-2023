from day2 import (
    GameSimulator,
    process_game_from_file,
    process_power_game_from_file,
)  # The code to test
import pytest
import os


def test_calculate_games_raises_error_on_empty_line():
    gs = GameSimulator(12, 13, 14)
    with pytest.raises(RuntimeError):
        gs.calculate_games([""])


def test_calculate_games_raises_error_on_None_line():
    gs = GameSimulator(12, 13, 14)
    with pytest.raises(RuntimeError):
        gs.calculate_games([None])


def test_calculate_games_returns_game_id_if_red_number_cubes_is_less_than_target_single_round():
    gs = GameSimulator(12, 13, 14)
    assert 1 == gs.calculate_games(["Game 1: 1 red"])


def test_calculate_games_returns_game_id_if_red_number_and_blue_number_cubes_is_less_than_target_single_round():
    gs = GameSimulator(12, 13, 14)
    assert 1 == gs.calculate_games(["Game 1: 1 red, 1 blue"])


def test_calculate_games_returns_game_id_if_red_blue_green_cubes_is_less_than_target_single_round():
    gs = GameSimulator(12, 13, 14)
    assert 1 == gs.calculate_games(["Game 1: 1 red, 1 blue, 1 green"])


def test_calculate_games_returns_0_if_red_is_larger_than_limit_single_round():
    gs = GameSimulator(12, 13, 14)
    assert 0 == gs.calculate_games(["Game 1: 100 red, 1 blue, 1 green"])


def test_calculate_games_returns_0_if_blue_is_larger_than_limit_single_round():
    gs = GameSimulator(12, 13, 14)
    assert 0 == gs.calculate_games(["Game 1: 100 blue, 2 green"])


def test_calculate_games_returns_0_if_green_is_larger_than_limit_single_round():
    gs = GameSimulator(12, 13, 14)
    assert 0 == gs.calculate_games(["Game 1: 4 red, 3 blue, 100 green"])


def test_calculate_games_ignores_order_single_round():
    gs = GameSimulator(12, 13, 14)
    assert 0 == gs.calculate_games(["Game 1: 100 green, 4 red, 3 blue"])
    assert 1 == gs.calculate_games(["Game 1: 1 green, 5 red, 3 blue"])


def test_calculate_games_returns_game_id_if_at_limits_single_round():
    gs = GameSimulator(12, 13, 14)
    assert 1 == gs.calculate_games(["Game 1: 13 green, 12 red, 14 blue"])


def test_calculate_games_returns_game_id_if_colour_is_has_been_after_multiple_rounds_round():
    gs = GameSimulator(12, 13, 14)
    assert 1 == gs.calculate_games(["Game 1: 1 green, 1 red, 1 blue; 1 green"])


def test_calculate_games_returns_game_id_if_colour_is_at_limit_after_multiple_rounds_round():
    gs = GameSimulator(12, 13, 14)
    assert 1 == gs.calculate_games(["Game 1: 1 green, 1 red, 1 blue; 13 green"])


def test_calculate_games_returns_0_if_colour_has_been_over_limit_after_multiple_rounds_round():
    gs = GameSimulator(12, 13, 14)
    assert 0 == gs.calculate_games(["Game 1: 1 green, 1 red, 1 blue; 14 green"])


def test_calculate_games_returns_sum_of_2_games_within_limit():
    gs = GameSimulator(12, 13, 14)
    assert 5 == gs.calculate_games(
        [
            "Game 1: 1 green, 12 red, 12 blue; 11 green",
            "Game 4: 12 green, 1 red, 14 blue; 13 blue",
        ]
    )


def test_calculate_games_returns_sum_of_2_games_within_limit_with_two_games_out_side_limt():
    gs = GameSimulator(12, 13, 14)
    assert 5 == gs.calculate_games(
        [
            "Game 1: 1 green, 12 red, 12 blue; 11 green",
            "Game 2: 12 green, 50 red, 1 blue; 12 blue",
            "Game 4: 12 green, 1 red, 1 blue; 13 blue",
            "Game 2: 12 green, 2 red, 1 blue; 15 blue",
        ]
    )


def test_calculate_power_games_returns_power_for_single_cube_single_round():
    gs = GameSimulator(12, 13, 14)
    assert 3 == gs.calculate_power_games(["Game 1: 3 red"])


def test_calculate_power_games_returns_power_for_multiple_cube_single_round():
    gs = GameSimulator(12, 13, 14)
    assert 8 == gs.calculate_power_games(["Game 1: 2 red, 4 blue"])
    assert 80 == gs.calculate_power_games(["Game 1: 2 red, 4 blue, 10 green"])


def test_calculate_power_games_returns_power_for_single_colour_multiple_rounds():
    gs = GameSimulator(12, 13, 14)
    assert 5 == gs.calculate_power_games(["Game 1: 2 blue; 5 blue"])


def test_calculate_power_games_returns_power_for_multiple_cube_multiple_rounds():
    gs = GameSimulator(12, 13, 14)
    assert 30 == gs.calculate_power_games(["Game 1: 2 green, 3 red, 2 blue; 5 green"])
    assert 12 == gs.calculate_power_games(["Game 1: 2 green, 3 red, 2 blue; 1 green"])


def test_calculate_games_returns_sum_of_2_game():
    gs = GameSimulator(12, 13, 14)
    assert 1752 == gs.calculate_power_games(
        [
            "Game 1: 1 green, 12 red, 12 blue; 11 green",
            "Game 4: 12 green, 1 red, 14 blue; 13 blue",
        ]
    )


def test_evaluate_day2_a_scenario_returns_expected_sum_for_test_document():
    gs = GameSimulator(12, 13, 14)
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "test_data/day_2_test_input.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    assert 8 == process_game_from_file(gs, abs_file_path)


def test_evaluate_day2_a_scenario_returns_expected_sum_for_read_data():
    gs = GameSimulator(12, 13, 14)
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "data_files/day2.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    assert 2006 == process_game_from_file(gs, abs_file_path)


def test_evaluate_day2_b_scenario_returns_expected_sum_for_test_document():
    gs = GameSimulator(12, 13, 14)
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "test_data/day_2_b_test_input.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    assert 2286 == process_power_game_from_file(gs, abs_file_path)
