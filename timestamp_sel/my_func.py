#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   hshi
#   E-mail  :   snapwings3190@163.com
#   Date    :   19/09/20 11:21:45
#   Desc    :

import os
import numpy as np

def get_min_abs(x):
    minabs = abs(x[0][0])
    global minele,matrix_index
    minele = x[0][0]
    matrix_index = x[0][1]
    for n in xrange(len(x)):
        if abs(x[n][0]) <= minabs:
            minabs = abs(x[n][0])
            minele = x[n][0]
            matrix_index = x[n][1]
        return minele,matrix_index

def timestamp_com(source, target):
    Arr_source = np.loadtxt(source, delimiter=',')
    Arr_target = np.loadtxt(target, delimiter=',')
    Arr_source_len = len(Arr_source)
    global Arr_source_temp,ori_list
    Arr_source_temp = []
    ori_list = []
    temp = (Arr_source[i] for i in xrange(Arr_source_len))
    for m in temp:
        matrix_ele_arr = np.where((Arr_target[:,0]>=m[0]-0.05) & (Arr_target[:,0]<=m[0]+0.05))
        if len(matrix_ele_arr[0]) >= 1:
            matrix_ele = (int(matrix_ele_arr[0][i]) for i in xrange(len(matrix_ele_arr[0])))
            global matrix_temp
            matrix_temp = []
            for s in matrix_ele:
                matrix_temp.append([m[0] - Arr_target[s][0], s])
            get_min_abs(matrix_temp)
            if abs(minele) <= 0.05:
                ori_list.append(Arr_target[matrix_index])
                Arr_source_temp.append(m)
    return Arr_source_temp,ori_list
#timestamp_com(os.getcwd()+'/ego_tar_pos_vel.csv', os.getcwd()+'/matrix_obs_vehicle.csv')
#np.savetxt('ori_list.csv', np.array(ori_list), delimiter = ',')
#np.savetxt('Arr_source_temp.csv', np.array(Arr_source_temp), delimiter = ',')
