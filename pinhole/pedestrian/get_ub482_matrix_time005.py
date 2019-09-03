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
odom_temp = odom

odom_len = len(odom)
obs_len = len(obs)
c = []
i = 0
j = 0
z = 0
odom_matri_time_diff = []
while i < odom_len:
    j = i + 1
#    print j
    a = [10000]
    b = [-10000]
    while j < obs_len:
        timestamp_min = odom[i][0] - obs[j][0]
        if timestamp_min >= 0:
            a.append(timestamp_min)
        else:
            b.append(timestamp_min)
        j += 1
    if min(a) >= abs(max(b)):
        if abs(max(b)) <= 0.05:
            obs_element = odom[i][0] - max(b)
            odom_matri_time_diff.append(abs(max(b)))
            g = np.where(obs == obs_element)
#            j = int(g[0])
#            print j
            c.append(obs[g[0][0]])
        else:
            odom_temp = np.delete(odom_temp, i-z, axis=0)
            z += 1
    else:
        if min(a) <= 0.05:
            obs_element = odom[i][0] - min(a)
            odom_matri_time_diff.append(min(a))
            g = np.where(obs == obs_element)
#            j = int(g[0])
#            print j
            c.append(obs[g[0][0]])
        else:
            odom_temp = np.delete(odom_temp, i-z, axis=0)
            z += 1
    i += 1
#print c
d = np.array(c)
e = np.delete(d, 0, axis=1)
odom_matri_time_diff.sort()
Arr_odom_matri_time_diff = np.array(odom_matri_time_diff)
#print "===="
#f = np.concatenate((odom,time_speed), axis=1)
#print odom.shape
#print e.shape
odom_speed = np.concatenate((odom_temp,e),axis=1)
print odom_speed
#c = a[np.where(a[:,1]>=150)]
#b= a[np.where((a[:,0]>0) & (a[:,0]<6))]
#np.savetxt('new.csv', f, delimiter = ',', header="timestamp, ub482Odom, ")
np.savetxt('pinhole_time_diff.csv', Arr_odom_matri_time_diff, delimiter = ',')
np.savetxt('ped_pinhole.csv', odom_speed, delimiter = ',',header="timestamp, ub482Odom, ub482speed, Ego_speed, ObsId, vehicle.x, vehicle.y, speed.x, speed.y, Life, Classification, CameraId")
