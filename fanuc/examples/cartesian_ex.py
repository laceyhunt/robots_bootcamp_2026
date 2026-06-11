#!/usr/bin/env python3
'''
This was the example code from Robotics 1 in Spring 2024 
demoing simple cartesian commands to the robot.
 updated 2/1/2024 by Kris Olds
 updated 6/11/2026 by Lacey Bowden
'''
import sys
sys.path.append('../src')
from robot_controller import robot
from time import sleep

robot_ip = '10.1.1.30'      # DJ (Uses Schunk Gripper)
# robot_ip = '10.1.1.31'      # Bill (uses OnRobot gripper)

my_robot = robot(robot_ip)
my_robot.set_speed(100)




# Read and print the current cartesian position
cur_pos = my_robot.read_current_cartesian_pose()
print(f"Current Position (Cart): {cur_pos}")

# Go to home position
home_pos = [540.0, -150.0, 550.0, -179.9, 0, 0]  # NOTE: The last three values are the W,P,R and must be in the range -179.9 and 179.9
my_robot.write_cartesian_position(home_pos)

cur_pos = my_robot.read_current_cartesian_pose()
print(f"Current Position (Cart): {cur_pos}")