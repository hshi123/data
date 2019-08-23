#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   hshi
#   E-mail  :   snapwings3190@163.com
#   Date    :   19/08/21 14:00:26
#   Desc    :   
import numpy as np
import csv

#obs = np.loadtxt('textobs.csv', delimiter=',')
obs = np.loadtxt('vehicleObstacle.csv', delimiter=',')
#odom = np.loadtxt('text.csv', delimiter=',')
odom = np.loadtxt('ub482Odom.csv', delimiter=',')
odom_temp = odom
#speed = np.loadtxt('ub482Speed.csv', delimiter=',')
#time_speed = np.delete(speed, 0,axis=1)

odom_len = len(odom)
obs_len = len(obs)
c = []
i = 0
j = 0
while i < odom_len:
    j = i + 1
    a = [100]
    b = [-100]
    while j < obs_len:
        timestamp_min = odom[i][0] - obs[j][0]
#        print '====='
#        print timestamp_min
        if timestamp_min >= 0:
            a.append(timestamp_min)
        else:
            b.append(timestamp_min)
        j += 1
#        print "j=", j
#    print a
#    print b
    if min(a) >= abs(max(b)):
        if abs(max(b)) <= 0.1:
            obs_element = odom[i][0] - max(b)
#        print obs_element
            g = np.where(obs == obs_element)
            c.append(obs[g[0][0]])
        else:
            odom_temp = np.delete(odom_temp, i, axis=0)
    else:
        if min(a) <= 0.1:
            obs_element = odom[i][0] - min(a)
#        print obs_element
            g = np.where(obs == obs_element)
            c.append(obs[g[0][0]])
        else:
            odom_temp = np.delete(odom_temp, i, axis=0)
    i += 1
#    print "i=", i

d = np.array(c)
e = np.delete(d, 0, axis=1)
#f = np.concatenate((odom,time_speed), axis=1)
#print odom.shape
#print e.shape
odom_speed = np.concatenate((odom_temp,e),axis=1)
#np.savetxt('new.csv', f, delimiter = ',', header="timestamp, ub482Odom, ")
np.savetxt('odom_speed.csv', g, delimiter = ',',header="timestamp, ub482Odom, ub482speed, ObsId, vehicle.x, vehicle.y, speed.x, speed.y, Life, Classification, CameraId")

