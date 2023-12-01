# advent-of-code-2023
Puzzle solutions for the advent of code 2023 challenge


# Set up
- Create a virtual environment
- Install requirements.txt to run the tests

# How to Run
- Activate the virtualenv
- run the advent_calendar_story.py

# Structure
- Each day is split into multiple files:
- - Python code
- - - day{n}.py - THe python code for the day
- - - test_day{n}.py - the unit test code for the day
- - - advent_calendar_story.py new function that calls the day files and writes the story
- - Test Data
- - - test_data/day_{n}_test_input.txt test input for the first half of the challenge
- - - test_data/day_{n}_b_test_data.txt test input for the second half of the challenge
- - Scenario Data
- - - data_files/day{n}.txt challenge data for the first half
- - - data_files/day{n}_b.txt challenge data for the second half

