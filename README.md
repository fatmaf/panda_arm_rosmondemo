> A package that contains a demo of ROSMonitoring for ROS2 using the moveit2 panda arm servo example 

### Setup 
_versions I used are in brackets_
* ROS 2 (Galactic)
* MoveIt2 (for Galactic)
  * [Install from here](https://moveit.picknik.ai/galactic/doc/tutorials/getting_started/getting_started.html)
  * **Replace `rosdep update` with `rosdep update --include-eol-distros`**: This is because galactic is an EOL distribution. If using the latest distro, this step is not needed

### Running things

_We will use the [Realtime Arm Servoing Example](https://moveit.picknik.ai/galactic/doc/examples/realtime_servo/realtime_servo_tutorial.html)_

* Connect the joystick 
* Detect it using: `ros2 run joy joy_node`
* In another terminal run `ros2 launch moveit_servo servo_example.launch.py`
* In another terminal run `ros2 service call /servo_node/start_servo std_srvs/srv/Trigger {}` (this starts the joystick control)



