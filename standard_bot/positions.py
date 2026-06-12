import math

def deg(*d):
    return tuple(math.radians(x) for x in d)

# *** Your recorded positions appear below ***************************
# Run get_pose.py to add positions here. Each one becomes a line like:
#     HOME = deg(114.4, 3.7, -81.2, -39.1, 100.5, -157.9)
# and you can then use it in standard_bot.py as:  positions.HOME