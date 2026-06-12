from standardbots import StandardBotsRobot, models
import positions
import time

# how to find the API token
# 1. Hit “Connect” button.
# 2. Type “0000” (4 zero’s).
# 3. Click on robot name (bottom lefthand corner).
# 4. Click “Settings”.
# 5. Click “Configure Developer API”.
# 6. Ensure “Enable Developer API” is turned on.
# 7. Gather “Authentication Token” value.

# robot connection info
ROBOT_URL = "http://10.1.1.42:3000"          # Simon
# ROBOT_URL = "http://10.1.1.41:3000"          # Theodore
API_TOKEN = "ya4-t7a8-rr4s-n89uk"            # Simon
# API_TOKEN = "8geqfqu0-qbbkig-ozwgr4-tl2xfj7" # Theodore

# positions come from positions.py (run get_pose.py to record your own).

# the robot object
sdk = StandardBotsRobot(
    url=ROBOT_URL,
    token=API_TOKEN,
    robot_kind=StandardBotsRobot.RobotKind.Live,
)

# move the robot to a joint position
def move(robot, joints, speed=0.8):
    req = models.ArmPositionUpdateRequest(
        kind=models.ArmPositionUpdateRequestKindEnum.JointRotation,
        joint_rotation=models.ArmJointRotations(joints=joints),
        movement_kind=models.MovementKindEnum.Joint,
        speed_profile=models.SpeedProfile(scaling_factor=speed),
    )
    robot.movement.position.set_arm_position(body=req)

# open the onRobot gripper
def open_gripper(width=0.062, force=10.0):
    with sdk.connection():
        gripper_command = models.GripperCommandRequest(
            kind=models.GripperKindEnum.Onrobot2Fg14,
            onrobot_2fg14=models.OnRobot2FG14GripperCommandRequest(
                grip_direction=models.LinearGripDirectionEnum.Outward,
                target_grip_width=models.LinearUnit(
                    value=width, unit_kind=models.LinearUnitKind.Meters
                ),
                target_force=models.ForceUnit(
                    value=force,
                    unit_kind=models.ForceUnitKind.Newtons,
                ),
                control_kind=models.OnRobot2FG14ControlKindEnum.Move,
            ),
        )
        res = sdk.equipment.control_gripper(gripper_command).ok()

# close the onRobot gripper
def close_gripper(width=0.035, force=10.0):
    with sdk.connection():
        gripper_command = models.GripperCommandRequest(
            kind=models.GripperKindEnum.Onrobot2Fg14,
            onrobot_2fg14=models.OnRobot2FG14GripperCommandRequest(
                grip_direction=models.LinearGripDirectionEnum.Outward,
                target_grip_width=models.LinearUnit(
                    value=width, unit_kind=models.LinearUnitKind.Meters
                ),
                target_force=models.ForceUnit(
                    value=force,
                    unit_kind=models.ForceUnitKind.Newtons,
                ),
                control_kind=models.OnRobot2FG14ControlKindEnum.Move,
            ),
        )
        res = sdk.equipment.control_gripper(gripper_command).ok()

# capture an image from the robot's camera
def capture_frame(robot, path="camera_frame.jpg"):
    import base64
    import numpy as np
    import cv2

    # camera settings required to operate the camera
    settings = models.CameraSettings(
        brightness=50, contrast=50, exposure=400,
        sharpness=50, hue=0, whiteBalance=4000, autoWhiteBalance=False,
    )
    # get a color frame from the camera
    response = robot.camera.data.get_color_frame(
        body=models.CameraFrameRequest(camera_settings=settings)
    )
    if response.isNotOk():
        # Show what actually went wrong so we can fix it
        print(f"Could not get a camera frame (status {response.status}).")
        if response.data is not None:
            print(f"   Reason: {response.data.message}")
        return None

    # decode the camera frame
    base64_data = response.response.data.decode().split(",")[1]
    image_bytes = base64.b64decode(base64_data)

    # convert camera frame to opencv image
    np_data = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_data, cv2.IMREAD_COLOR)

    # save the image
    cv2.imwrite(path, img)
    print(f"Image saved to {path}")
    return img

# main pick-and-place routine
def main():
    # connect to the robot
    robot = StandardBotsRobot(
        url=ROBOT_URL,
        token=API_TOKEN,
        robot_kind=StandardBotsRobot.RobotKind.Live,
    )

    # connect to robot
    with robot.connection():

        # sanity check to see if robot is reachable
        if robot.movement.position.get_arm_position().isNotOk():
            print("Could not connect to robot. Check the URL and token.")
            return

        # take control of robot (not sure if this is necessary)
        robot.status.control.set_configuration_control_state(
            body=models.RobotControlMode(kind=models.RobotControlModeEnum.Api)
        )

        print("Starting routine...")

        # *******************************************************************
        #  YOUR ROUTINE GOES HERE
        #
        #  1. run get_pose.py to record positions. Name them whatever you
        #     like (for example: HOME, ABOVE_PICK, PICK, PLACE, CAMERA).
        #  2. sample commands are located below for using to build your
        #     routine.
        # *******************************************************************

        # how to open the gripper
        # open_gripper()
        # time.sleep(0.5)

        # move the robot with a joint movement
        # move(robot, positions.HOME)
        # time.sleep(1)

        # close the gripper
        # close_gripper()
        # time.sleep(1)

        # capture an image from the robot's camera
        capture_frame(robot)


if __name__ == '__main__':
    main()
