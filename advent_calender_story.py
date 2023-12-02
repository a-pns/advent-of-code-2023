import os
from day1 import evaluate_day1_scenario, evaluate_day1_b_scenario
from day2 import (
    GameSimulator,
    process_game_from_file,
    process_power_game_from_file,
)  # The code to test


def return_abs_path(relative_string):
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    return os.path.join(script_dir, relative_string)


def day_1_story():
    print("Day 1 ----- Saving Christmas ------")
    print(
        """
        After being almost sent out fo the Trebuchet in the wrong direction 
        becuase of the scurilous elves, I had to do some investigation of the callibration numbers...
        """
    )
    print(
        f"The callibration sums needed for the Trebuchet is: {evaluate_day1_scenario(return_abs_path('data_files/day1_a.txt'))}"
    )
    print(
        """
        Ah HA!!! this number was correct, but wait?.... they told me not to take tha actual digits, 
        but the digits are spelt out!!! Good Job I did not actually get in that catapult... right lets calculate it again
        """
    )
    print(
        f"The callibration sums needed for the Trebuchet (using spelt out digits) is: {evaluate_day1_b_scenario(return_abs_path('data_files/day1_b.txt'))}"
    )
    print(
        """
        YESSSS, YESSSS the calibration is a success... at least they think sooo....... 3 ... 2 ... 1 ...
           UP UP and AWAY!!!!!!!!!!!!!!!!!!!!!!
        """
    )


def day_2_story():
    print(
        """
        Sooooo....... I'm now on this magical snow island where all the snow comes from (looks 
        like I'm going to have to reavaluate my understanding of science)
        Any way we are going for a bit of a walk (to find snow?) but anyway there is this stupid game
        that seems impossible to solve - trying to work out how many cubes of each colour are there.

        However, there a little more interesting game to see how many games would have been possible
        if we already new the limits,

        So here goes....
        """
    )
    print(
        "Sum of the total games that would have been possible if the limit was: only 12 red cubes, 13 green cubes, and 14 blue cubes"
    )
    gs = GameSimulator(12, 13, 14)
    print(
        f"it was.....{process_game_from_file(gs, return_abs_path('data_files/day2.txt'))}"
    )
    print(
        """
        Sooooo....... that was a pointless game, but at least we've got somewhere on the trip!
        Looks like if there is no water then snow cannot be mate (who would have thought eh!)
        Anyway they are not sure why it's stopped but now want me to check

        Looks like I''m the only one to do anything around here, but the gist here is.... wait it's 
        this stupid games again. now i need to work out the fewest cubes in each game, then times
        these together and then sum them up!

        okay... here goes!
        """
    )

    print(
        f"it was.....{process_power_game_from_file(gs, return_abs_path('data_files/day2_b.txt'))}"
    )


if __name__ == "__main__":
    day_1_story()
    day_2_story()
