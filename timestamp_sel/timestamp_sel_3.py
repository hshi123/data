#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   hshi
#   E-mail  :   snapwings3190@163.com
#   Date    :   19/10/09 19:37:14
#   Desc    :   
from time import time
import my_func
import os
import numpy as np

if __name__ == '__main__':
    t = time()
    my_func.timestamp_com(os.getcwd()+'/ego_tar_pos_vel.csv', os.getcwd()+'/matrix_obs_vehicle.csv')
    final_target = np.delete((np.array(my_func.ori_list)), 0, axis=1)
    final_arr = np.concatenate(((np.array(my_func.Arr_source_temp)), final_target), axis=1)
    np.savetxt('matrix_vehicle_detection.csv', final_arr, delimiter = ',', header="timestamp, ego_position.x, ego_position.y, ego_vel.x, ego_vel.y, tar_position.x, tar_position.y, tar_vel.x, tar_vel.y, relative_dis, relative_vel, ObsId, CameraId, Classification, LifeTime, distance.x, distance.y, vel.x, vel.y, ObsTheta, Length, Width, Height")
    print len(my_func.Arr_source_temp)
    print len(my_func.ori_list)
    print "total run time:"
    print time()-t
