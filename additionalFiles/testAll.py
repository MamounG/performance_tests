#!/usr/bin/env python
from subprocess import Popen
from time import sleep
from os import remove
import matplotlib.pyplot as plt
import sys  

files = ["CppToCpp", "CppToPython", "PythonToCpp", "PythonToPython"]

def startSub(nodeToStart):
    proc = Popen(["rosrun", "performance_tests", nodeToStart])
    return proc
    
def startPub(nodeToStart,rate,nbTests):
    proc = Popen(["rosrun", "performance_tests", nodeToStart, rate, nbTests])
    return proc
    
def oneTest(pub,subs,rate,nbTests):
    procSub = startSub(subs)
    sleep(1)
    procPub = startPub(pub, rate, nbTests)
    
    stdoutdata, stderrdata = procPub.communicate()
    if (procPub.returncode == 0):
        #procPub.kill()
        procSub.kill()



def allTestForOneRate(rate,nbTests):
    oneTest("pub","subs",rate,nbTests)
    oneTest("pub","subscriber.py",rate,nbTests)
    oneTest("publisher.py","subs",rate,nbTests)
    oneTest("publisher.py","subscriber.py",rate,nbTests)
    
    
def retrieveFromFile(f):
    with open(f) as fi:
        content = fi.readlines()
    content = [r.strip() for r in content]
    x = []
    y = []
    for c in content:
        xVal = c.split("|")[0]
        yVal = float(c.split("|")[1]) - 1/float(xVal)
        x.append(xVal)
        y.append(str(yVal))
    print x
    print y
    return x,y
    
    
#start of script
if (len(sys.argv) != 3):
    print("FAIL")
    print("usage: ./testAll.py [rateToTestFile] [nbTests]")
else:
    with open(sys.argv[1]) as f:
        rates = f.readlines()
    rates = [x.strip() for x in rates] 
    for r in rates:
        print("testing rate: " +r)
        allTestForOneRate(r,sys.argv[2])
        
    for f in files:
        x,y = retrieveFromFile(f)
        plt.plot(x,y, label=f)
    plt.legend()
    plt.show()
    
    for f in files:
        remove(f)
#argv: rate file, nbTests

#read file: ratesTotests (arv)

#foreach rate run oneTest

#draw curve

#remove relevant files
