from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.A)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Go forward and backwards for one meter.
robot.straight(1000)
ev3.speaker.beep()

robot.straight(-1000)
ev3.speaker.beep()

# Turn clockwise by 360 degrees and back again.
robot.turn(360)
ev3.speaker.beep()

robot.turn(-360)
ev3.speaker.beep()