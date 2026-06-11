#!/usr/bin/env python3
'''
Simple conveyor belt demo bounces an object back and forth between proximity sensors

Created 6/11/2026 by Lacey Bowden
'''

import sys
sys.path.append('../src')
from robot_controller import robot
from time import sleep

robot_ip = '10.1.1.30'      # DJ (Uses Schunk Gripper)
# robot_ip = '10.1.1.31'      # Bill (uses OnRobot gripper)

my_robot = robot(robot_ip)

print('Moving conveyor left until sensor broken...')

while True:
   # Turn on conveyor reverse (so die moves left)
   my_robot.conveyor('reverse')
   prox_sensor=0
   # While proximity sensor not broken
   while not prox_sensor:
      # Check sensor
      prox_sensor=my_robot.conveyor_proximity_sensor('left')
      # Sleep to allow sensor to read
      sleep(0.1)
   # Stop conveyor
   my_robot.conveyor('stop')

   print('Die reached left side! Going back...')
   sleep(1)
   
   # Turn on conveyor forward (so die moves right)
   my_robot.conveyor('forward')
   prox_sensor=0
   # While proximity sensor not broken
   while not prox_sensor:
      # Check sensor
      prox_sensor=my_robot.conveyor_proximity_sensor('right')
      # Sleep to allow sensor to read
      sleep(0.1)
   # Stop conveyor
   my_robot.conveyor('stop')
   
   print('Die reached right side! Going back...')
   sleep(1)