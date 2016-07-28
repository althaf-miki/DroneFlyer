#!/usr/bin/env python
import rospy
from mavros.srv import SetMode, CommandBool, CommandTOL
import time

def take_off_and_land():

    rospy.init_node('mavros_takeoff_python')
    rate = rospy.Rate(10)

    ####
    # GUIDED
    ####
    rospy.wait_for_service('/mavros/set_mode')
    try:
        change_mode = rospy.ServiceProxy('/mavros/set_mode', SetMode)
        resp = change_mode(custom_mode="GUIDED")
        print "setmode send ok %s"%resp.success
    except rospy.ServiceException, e:
        print "Failed SetMode: %s"%e

    ###
    # ARM
    ###
    rospy.wait_for_service('/mavros/cmd/arming')
    try:
        arming_cl = rospy.ServiceProxy('/mavros/cmd/arming', CommandBool)
        resp = arming_cl(value = True)
        print "ARM send ok %s"%resp.success
    except rospy.ServiceException, e:
        print "Failed arming or disarming"

    ###
    # LAND
    ###
    rospy.wait_for_service('/mavros/cmd/takeoff')
    try:
        takeoff_cl = rospy.ServiceProxy('/mavros/cmd/takeoff', CommandTOL)
        resp = takeoff_cl(altitude=10, latitude=0, longitude=0, min_pitch=0, yaw=0)
        print "srv_land send ok %d"%resp.success
    except:
        print "Failed Land"


    time.sleep(5)

    ###
    # LAND
    ###
    rospy.wait_for_service('/mavros/cmd/land')
    try:
        takeoff_cl = rospy.ServiceProxy('/mavros/cmd/land', CommandTOL)
        resp = takeoff_cl(altitude=10, latitude=0, longitude=0, min_pitch=0, yaw=0)
        print "srv_land send ok %d"%resp.success
    except:
        print "Failed Land"


if __name__ == '__main__':
    try:
        take_off_and_land()
    except:
        pass
