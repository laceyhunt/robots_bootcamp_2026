#!/usr/bin/env python3
'''
Simple joint movement example code

Created 6/11/2026 by Lacey Bowden
'''
import sys
sys.path.append('../src')
from robot_controller import robot
from time import sleep

robot_ip = '10.1.1.30'      # DJ (Uses Schunk Gripper)
# robot_ip = '10.1.1.31'      # Bill (uses OnRobot gripper)

# Initialize Robot
my_robot = robot(robot_ip)
my_robot.set_speed(100)




# Read and print the current joint position
joint_pose = my_robot.read_current_cartesian_pose()
print(f"Current Position (Joint): {joint_pose}")

# Go to home position
home_pos_joint = [0.0, 0.0, 0.0, 0.0, -90.0, 30.0]   # NOTE: all values must be floats and within the range -179.9 and 179.9
my_robot.write_joint_pose(home_pos_joint)
   
# Read and print the current joint position
joint_pose = my_robot.read_current_cartesian_pose()
print(f"Current Position (Joint): {joint_pose}")