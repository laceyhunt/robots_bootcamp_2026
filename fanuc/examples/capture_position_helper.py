import os
import sys
sys.path.append('../src')
from robot_controller import robot

# Global Constants
robot_ip = '10.1.1.30'      # DJ (Uses Schunk Gripper)
# robot_ip = '10.1.1.31'      # Bill (uses OnRobot gripper)

my_robot = robot(robot_ip)

def write_to_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write(text+ '\n')

current_directory = os.getcwd()

file_path = os.path.join(current_directory, 'position_log.txt')
pose_num = 1

while True:
    choice = input("Please choose an option:\n1. Capture Position\n2. Quit program\n")

    if choice == "1":
        # Code to capture position goes here
        text = "pose " + str(pose_num) + ": " + str(my_robot.read_current_joint_position())
        write_to_file(file_path, text)
        print("Position captured!")
        pose_num += 1

    elif choice == "2":
        print("Quitting the program...")
        break

    else:
        print("Invalid choice. Please try again.")
