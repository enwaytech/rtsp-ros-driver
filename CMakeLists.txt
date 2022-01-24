cmake_minimum_required(VERSION 3.1)
project(rtsp_ros_driver)

set(PROJECT_CATKIN_DEPS
      camera_info_manager_py
      cv_bridge
      rospy
      sensor_msgs
      std_srvs
)

# Only add build dependencies, not runtime
find_package(catkin REQUIRED
  COMPONENTS
    ${PROJECT_CATKIN_DEPS}
)

catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS
    ${PROJECT_CATKIN_DEPS}
)

########################################################
# Installs
########################################################

file(GLOB NODES src/*)
catkin_install_python(
  PROGRAMS
    ${NODES}
  DESTINATION
    ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

