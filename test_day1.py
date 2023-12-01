from day1 import (
    evaluate_line,
    evaluate_multiple_lines,
    evaluate_day1_scenario,
    evaluate_multiple_spelt_lines,
    evaluate_day1_b_scenario,
)  # The code to test
import pytest
import os


def test_evaluate_line_returns_error_when_line_length_is_empty():
    with pytest.raises(RuntimeError):
        evaluate_line("")


def test_evaluate_line_returns_concatendated_digit_if_the_digit_is_the_only_char_in_line():
    evaluate_line("1") == 11


def test_evaluate_line_returns_error_when_does_not_have_a_digit():
    with pytest.raises(RuntimeError):
        evaluate_line("test")


def test_evaluate_line_concatenates_digit_to_itself_when_line_has_only_1_digit():
    assert evaluate_line("1test") == 11


def test_evaluate_line_returns_sum_of_starting_and_ending_digits():
    assert evaluate_line("1test5") == 15


def test_evaluate_line_returns_sum_of_first_and_last_digits():
    assert evaluate_line("t1es9t") == 19


def test_evaluate_line_returns_sum_of_first_and_last_digits_when_there_are_more_than_3():
    assert evaluate_line("t1e2s9t") == 19


def test_evaluate_multiple_lines_returns_sum_for_single_line():
    assert evaluate_multiple_lines(["1test5"]) == 15


def test_evaluate_multiple_lines_returns_sum_for_multiple_lines():
    assert evaluate_multiple_lines(["1test5", "5t9"]) == 74


def test_evaluate_multiple_lines_returns_sum_for_multiple_lines_with_more_than_2_digits_a_line():
    assert (
        evaluate_multiple_lines(
            ["1test5", "5t9", "gsfgfds5gfdgfdsgfdsg6dsgfdgfds8gfdsgfdsgdf4"]
        )
        == 128
    )


def test_evaluate_day1_scenario_returns_expected_sum_for_test_document():
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "test_data/day_1_test_input.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    assert evaluate_day1_scenario(abs_file_path) == 142


def test_evaluate_day1_scenario_returns_expected_sum_for_day_1_a_document():
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "data_files/day1_a.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    assert evaluate_day1_scenario(abs_file_path) == 54561


def test_evaluate_multiple_spelt_lines_returns_sum_for_single_line():
    assert evaluate_multiple_spelt_lines(["onetestfive"]) == 15


def test_evaluate_multiple_spelt_lines_returns_sum_for_multiple_lines():
    assert evaluate_multiple_spelt_lines(["onetestfive", "fiveanine"]) == 74


def test_evaluate_multiple_spelt_lines_returns_sum_for_multiple_lines_with_more_than_2_digits_a_line():
    assert (
        evaluate_multiple_spelt_lines(
            [
                "eightwothree1",
                "fiveanine",
                "gsfgfdsfivegfdgfdsgfdsgsixdsgfdgfdseightgfdsgfdsgdffour9",
            ]
        )
        == 199
    )


def test_evaluate_multiple_spelt_lines_returns_sum_when_using_all_spelt_digits():
    assert (
        evaluate_multiple_spelt_lines(
            [
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine",
            ]
        )
        == 495
    )


def test_evaluate_multiple_spelt_lines_returns_sum_when_using_mix_of_digits_and_numbers():
    assert (
        evaluate_multiple_spelt_lines(
            [
                "one2",
                "1two",
                "three5",
                "four",
                "64five",
                "six",
                "seven1234",
                "9eight",
                "nine",
            ]
        )
        == 505
    )


def test_evaluate_multiple_spelt_lines_returns_sum_when_using_all_spelt_digits():
    assert (
        evaluate_multiple_spelt_lines(
            [
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine",
            ]
        )
        == 495
    )


def test_evaluate_day1_b_scenario_returns_expected_sum_for_test_document():
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "test_data/day_1_b_test_input.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    assert evaluate_day1_b_scenario(abs_file_path) == 281


def test_evaluate_day1_b_scenario_returns_expected_sum_for_real_data():
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "data_files/day1_a.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    assert evaluate_day1_b_scenario(abs_file_path) == 54076
