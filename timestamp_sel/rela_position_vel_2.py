#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   hshi
#   E-mail  :   snapwings3190@163.com
#   Date    :   19/09/19 18:01:24
#   Desc    :   

import numpy as np
from time import time

t = time()

ego_position = np.loadtxt('position_vel.csv', delimiter=',', usecols=(1,2))
tar_position = np.loadtxt('position_vel.csv', delimiter=',', usecols=(5,6))
ego_vel = np.loadtxt('position_vel.csv', delimiter=',', usecols=(3,4))
tar_vel = np.loadtxt('position_vel.csv', delimiter=',', usecols=(7,8))


position_len = len(ego_position)
i = 0
l = []
while i < position_len:
    temp = []
    position = np.sqrt(np.sum(np.square(ego_position[i] - tar_position[i])))
    vel = np.sqrt(np.sum(np.square(ego_vel[i] - tar_vel[i])))
    temp = [position, vel]
    l.append(temp)
    i += 1
Arr_position_vel = np.loadtxt('position_vel.csv', delimiter=',')

ego_tar_pos_vel = np.concatenate((Arr_position_vel, np.array(l)), axis=1)
np.savetxt('ego_tar_pos_vel.csv', ego_tar_pos_vel, delimiter=',')

print "total run time:"
print time()-t
