#!/usr/bin/env python3
"""! @brief Example python program using robot_controller.py
        Opens and Closes the Schunk gripper in a loop"""

# Imports
import time
import sys
sys.path.append('../src')
from robot_controller import robot

# Global Constants
robot_ip = '10.1.1.30'      # DJ (Uses Schunk Gripper)
total_loops = 3

def main():
    """! Main program entry"""

    # Create new robot object
    crx10 = robot(robot_ip)

    # Set robot speed
    crx10.set_speed(300)

    loops = 1
    while(loops <= total_loops):
        
        print("==============================")
        print(f"Current loops: {loops}/{total_loops}")
        print("==============================")

        # Open Gripper
        crx10.gripper('open')
        time.sleep(2)

        # Close Gripper
        crx10.gripper('close')
        time.sleep(2)

        # increment loops
        loops += 1

    # End program
    print("==============================")
    print("END OF PROGRAM")
    print("==============================")

if __name__=="__main__":
    main()
