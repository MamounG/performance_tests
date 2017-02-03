# performance_tests
performance tests between python and c++ with ROS

# Usage
In order to test the performamces, 4 files has been developed: 1 cpp publisher, 1 cpp subscriber, 1 python publisher, and 1 python subscriber. They can be run as follow:

rosrun performance_tests pub 10 10 # those are the rate and the number of msg to send
rosrun performance_tests subs
rosrun performance_tests publisher.py 10 10 # those are the rate and the number of msg to send
rosrun performance_tests subscriber.py

# To test perfomances
I provided also an additional Python scrypt to make and show the tests. You can run it from ~/performance_tests/additionalFiles/testAll.py rateFile 20

rateFile should be a file containing different rates to test (one rate per line) an example is given (~/performance_tests/additionalFiles/ratesToTest) and 20 is the number of messages to be send from each publisher. 

It shows the result under the form of 4 different curves (one for each combination) with the x axis as the rates tested and the y axis the average difference between the input rate and the rate computed.
