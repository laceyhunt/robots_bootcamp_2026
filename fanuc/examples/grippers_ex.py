#!/usr/bin/env python3
'''
Simple gripper movement example code
DJ uses Schunk, Bill uses OnRobot
Comment out the code you don't need

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



"""
   This code is for DJ (Schunk Gripper)
         it WILL NOT WORK for Bill
         make sure you double check your robot ip
"""
# Open Gripper
my_robot.gripper('open')
sleep(2)
# Close Gripper
my_robot.gripper('close')
sleep(2)



"""
   This code is for Bill (OnRobot Gripper)
         it WILL NOT WORK for DJ 
         make sure you double check your robot ip
"""
# The OnRobot gripper requires these extra parameters
open_width = 100
close_width = 78
force = 40

# Open gripper
my_robot.onRobot_gripper(open_width,force)
sleep(2)
# Close gripper
my_robot.onRobot_gripper(close_width,force)
sleep(2)
