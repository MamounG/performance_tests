#!/usr/bin/env python
import rospy
from performance_tests.msg import SuperAwesome

time1 = 0
sumTime = 0
nb = 0
firstUsage = True
rep = "additionalFiles/"

def writeToFile(sumToWrite, rate, serverType):
    global rep
    fileName =  serverType + "ToPython" 
    #rospy.loginfo(rospy.get_caller_id() +" fileName = %s", fileName)
    
    myfile = open(fileName, "a")
    myfile.write(str(rate)+"|"+str(sumToWrite)+"\n")
    myfile.close()



def callback(data):

    global firstUsage
    global sumTime
    global nb
    global time1

    
    time2 = rospy.get_time()
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.s)
    if "FIN" in data.s:
        #rospy.loginfo(rospy.get_caller_id() + " ending process")
        serverInfo = data.s.split("|")
        writeToFile((sumTime/nb),serverInfo[2],serverInfo[1])
        return
        

    if firstUsage:
        firstUsage = False
    else:
        sumTime += time2 - time1;
        nb+=1;
        #rospy.loginfo("curent time average = %f s", (sumTime/nb));
    time1 = rospy.get_time()
    
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("SuperTopic", SuperAwesome, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

