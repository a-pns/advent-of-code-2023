import os
from day1 import evaluate_day1_scenario, evaluate_day1_b_scenario


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


if __name__ == "__main__":
    day_1_story()
