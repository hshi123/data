#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   hshi
#   E-mail  :   snapwings3190@163.com
#   Date    :   19/08/21 14:00:26
#   Desc    :   
import numpy as np

obs = np.loadtxt('pedObstacle.csv', delimiter=',')
odom = np.loadtxt('ub482Odom.csv', delimiter=',')

odom_len = len(odom)
obs_len = len(obs)
c = []
i = 0
j = 0
while i < odom_len:
    #j = i + 1
   # j = 
    a = [10000]
    b = [-10000]
    while j < obs_len:
        timestamp_min = odom[i][0] - obs[j][0]
        if timestamp_min >= 0:
            a.append(timestamp_min)
        else:
            b.append(timestamp_min)
        j += 1
    print min(a)
    print max(b)
    if min(a) >= abs(max(b)):
        obs_element = odom[i][0] - max(b)
        print obs_element
        g = np.where(obs == obs_element)
#        print g
        print type(g)
        print int(g[0])
        j = int(g[0])
        c.append(obs[g[0][0]])
    else:
        obs_element = odom[i][0] - min(a)
        print obs_element
        g = np.where(obs == obs_element)
        print i
        print g
        print int(g[0])
        j = int(g[0])
        c.append(obs[g[0][0]])
    i += 1
    print "======"

d = np.array(c)
e = np.delete(d, 0, axis=1)
odom_speed = np.concatenate((odom,e),axis=1)
np.savetxt('ped_fisheye.csv', odom_speed, delimiter = ',',header="timestamp, ub482Odom, ub482speed, Ego_speed, ObsId, vehicle.x, vehicle.y, speed.x, speed.y, Life, Classification, CameraId")
