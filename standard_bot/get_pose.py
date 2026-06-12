from standardbots import StandardBotsRobot
import math, os

# robot connection info
# uncomment the credentials for the robot you are using 
ROBOT_URL = "http://10.1.1.42:3000"          # Simon
# ROBOT_URL = "http://10.1.1.41:3000"          # Theodore
API_TOKEN = "ya4-t7a8-rr4s-n89uk"            # Simon
# API_TOKEN = "8geqfqu0-qbbkig-ozwgr4-tl2xfj7" # Theodore


# define name of positions module
POSITIONS_FILE = "positions.py"

# to be placed at top of positions.py when when created
HEADER = (
    "import math\n"
    "\n"
    "def deg(*d):\n"
    "    return tuple(math.radians(x) for x in d)\n"
    "\n"
)

# read the robot's current joint angles (in degrees)
def read_joints_degrees(robot):
    response = robot.movement.position.get_arm_position()
    if response.isNotOk():
        return None
    joints_radians = response.ok().joint_rotations
    return [round(math.degrees(j), 1) for j in joints_radians]

# add one position to positions.py as a constant
def save_position(name: str, joints_degrees: tuple):
    # write the header once, the first time the file is created
    if not os.path.exists(POSITIONS_FILE):
        with open(POSITIONS_FILE, "w") as f:
            f.write(HEADER)
    # example:  HOME = deg(114.4, 3.7, -81.2, -39.1, 100.5, -157.9)
    angles = ", ".join(str(a) for a in joints_degrees)
    with open(POSITIONS_FILE, "a") as f:
        f.write(f"{name} = deg({angles})\n")

# main: move the robot, name the position, enter to save
def main():
    robot = StandardBotsRobot(
        url=ROBOT_URL,
        token=API_TOKEN,
        robot_kind=StandardBotsRobot.RobotKind.Live,
    )

    with robot.connection():
        print("Move the robot to a position, then type a name and press Enter.")
        print("Type 'q' and press Enter when you are finished.\n")

        while True:
            name = input("Position name (or 'q' to quit): ").strip()

            if name == "q":
                break
            if name == "":
                print("Please type a name.\n")
                continue

            # tidy the name so it can be used in code, e.g. "above pick" -> "ABOVE_PICK"
            name = name.upper().replace(" ", "_")

            # The name must be usable as positions.<name> in your program
            if not name.isidentifier():
                print("Please use letters, numbers and spaces only (not starting with a number).\n")
                continue

            joints = read_joints_degrees(robot)
            if joints is None:
                print("Could not read the robot position. Try again.\n")
                continue

            save_position(name, joints)
            print(f"Saved {name} = deg({', '.join(str(a) for a in joints)})\n")

    print(f"\nAll done! Your positions are in {POSITIONS_FILE}.")

if __name__ == "__main__":
    main()
