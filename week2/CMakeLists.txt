cmake_minimum_required(VERSION 2.8.3)
project(week2) #test_pkg)

find_package(catkin REQUIRED COMPONENTS
  #roscpp
  rospy
  std_msgs
  sensor_msgs
  message_generation
)

add_message_files(
  FILES
  flo.msg
)

add_service_files(
  FILES
 #AddTwopoints.srv 
 #trajectory.srv
  values.srv
  data.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
  sensor_msgs
)

catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs message_runtime sensor_msgs
#  include_directories( 
#  ${catkin_INCLUDE_DIRS}
  )
#)

#catkin_python_setup()
#catkin_install_python(PROGRAMS scripts/hello	scripts/listener
#                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})


