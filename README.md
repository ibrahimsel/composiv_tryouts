# Composiv Tryouts

## Create a catkin workspace

1.  For a linux system, you would go: `mkdir -p ~/catkin_ws/src`

2.  Assuming you have ROS (not ROS2!) installed on your system, you should go ahead and source your ROS with `source /opt/ros/${ROS_DISTRO}/setup.bash`

3. Then build the workspace with `catkin_make` while you're under the `~/catkin_ws` folder

4. After building, run `source devel/setup.bash` in the workspace folder

5. If everything went right, when you run `roslaunch composiv_tryouts composiv_tryout.launch` you should see the nodes `composiv_talker` and `composiv_listener` up and running