Readme file for CS534 Assignment 4

To run this code you need run simulation.py and input in the format of
   "sarsa goal_value pit_value step_penalty give_up_value num_trails epsilon"

Here is an example of the input:
sarsa 5 -2 -0.1 -3 10000 0.1

This means goal_value of 5, pit_value of -2, step_penalty of -0.1, give_up_value of -3, 10000 trails and epsilon value
of 0.1.

The output will have two parts:
1. The first part is a map of recommended action
2. The second part is a list of expect rewards for different states of all possible actions