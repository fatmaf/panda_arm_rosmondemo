> A package that contains a demo of ROSMonitoring for ROS2 using the moveit2 panda arm servo example 

### Setup 
_versions I used are in brackets_
* ROS 2 (Galactic)
* MoveIt2 (for Galactic)
  * [Install from here](https://moveit.picknik.ai/galactic/doc/tutorials/getting_started/getting_started.html)
  * **Replace `rosdep update` with `rosdep update --include-eol-distros`**: This is because galactic is an EOL distribution. If using the latest distro, this step is not needed
* ROSMonitoring for ROS 2 - get it from here please https://github.com/fatmaf/ROSMonitoring/tree/ros2port (we want the ros2port branch)


### Running things

_We will use the [Realtime Arm Servoing Example](https://moveit.picknik.ai/galactic/doc/examples/realtime_servo/realtime_servo_tutorial.html)_


**SOURCE moveit ws**


* Connect the joystick 
* Detect it using: `ros2 run joy joy_node`
* In another terminal run `ros2 launch moveit_servo servo_example.launch.py`
* In another terminal run `ros2 service call /servo_node/start_servo std_srvs/srv/Trigger {}` (this starts the joystick control)

* In another terminal navigate to the ROSMonitoring folder go to the oracle, go to LamaConvOracle and then type in `./oracle.py --property joint_pos_lim_prop --online --tense future --port 8080`
* In another terminal run `ros2 launch monitor monitor.launch`
* display the monitor verdict topic


