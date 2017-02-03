cmake_minimum_required(VERSION 2.8.3)
project(performance_tests)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  genmsg
)

## Generate messages in the 'msg' folder
 add_message_files(
   FILES
   SuperAwesome.msg
 )

## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs
 )

catkin_package()

###########
## Build ##
###########
include_directories(
  ${catkin_INCLUDE_DIRS}
)


include_directories(include ${catkin_INCLUDE_DIRS})

add_executable(pub src/publisher.cpp)
target_link_libraries(pub ${catkin_LIBRARIES})
add_dependencies(pub performance_tests_generate_messages_cpp)

add_executable(subs src/subscriber.cpp)
target_link_libraries(subs ${catkin_LIBRARIES})
add_dependencies(subs performance_tests_generate_messages_cpp)

