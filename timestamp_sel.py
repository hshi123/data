#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   hshi
#   E-mail  :   snapwings3190@163.com
#   Date    :   19/09/20 11:21:45
#   Desc    :   

import numpy as np
from time import time

def timestamp_com(source='ego_tar_pos_vel.csv', target='matrix_obs_vehicle.csv'):
    Arr_source = np.loadtxt(source, delimiter=',')
    Arr_target = np.loadtxt(target, delimiter=',')
    Arr_source_len = len(Arr_source)
    Arr_target_len = len(Arr_target)
    source_ori = abs(Arr_source[Arr_source_len-1][0] - Arr_target[0][0])
    target_ori = abs(Arr_target[Arr_target_len-1][0] - Arr_source[0][0])
    if source_ori > target_ori:
        ori = int(source_ori) + 1
    else:
        ori = int(target_ori)+ 1
    global Arr_source_temp,ori_list
    Arr_source_temp = []
    ori_list = []
    time_diff = []
    diff_ori = [0]
    temp = (Arr_source[i] for i in xrange(Arr_source_len))
    for m in temp:
        ori_plus = [ori]
        ori_minus = [-ori]
        if len(diff_ori) == 1:
            timestamp_diff = (m[0] - Arr_target[first_com][0] for first_com in xrange(Arr_target_len))
            for n in timestamp_diff:
                if n >= 0:
                    ori_plus.append(n)
                else:
                    ori_minus.append(n)
            if min(ori_plus) >= abs(max(ori_minus)):
                if abs(max(ori_minus)) <= 0.05:
                    target_element = m[0] - max(ori_minus)
                    #print tar_element
                    time_diff.append(abs(max(ori_minus)))
                    target_ori = np.where(Arr_target == target_element)
                   # print target_ori
                    if len(target_ori[0]) == 1:
                        target_ori1 = target_ori[0][0]
                        diff_ori.append(int(target_ori1))
                        ori_list.append(Arr_target[target_ori1])
                        Arr_source_temp.append(m)
                    elif len(target_ori[0]) > 1:
                        for k in xrange(len(target_ori)):
                            target_ori1 = target_ori[0][k]
                            diff_ori.append(int(target_ori1))
                            if Arr_target[target_ori1][3] == 1:
                                ori_list.append(Arr_target[target_ori1])
                                Arr_source_temp.append(m)
                            else:
                                pass
                    else:
                        print "Can't find value file target"
                else:
                    pass
            else:
                if min(ori_plus) <= 0.05:
                    target_element = m[0] - min(ori_plus)
                   # print target_element
                    time_diff.append(min(ori_plus))
                    target_ori = np.where(Arr_target == target_element)
                   # print target_ori1
                    if len(target_ori[0]) == 1:
                        target_ori1 = target_ori[0][0]
                        diff_ori.append(int(target_ori1))
                        ori_list.append(Arr_target[target_ori1])
                        Arr_source_temp.append(m)
                    elif len(target_ori[0]) > 1:
                        for k in xrange(len(target_ori)):
                            target_ori1 = target_ori[0][k]
                            diff_ori.append(int(target_ori1))
                            if Arr_target[target_ori1][3] == 1:
                                ori_list.append(Arr_target[target_ori1])
                                Arr_source_temp.append(m)
                            else:
                                pass
                    else:
                        print "Can't find value from file target"
                else:
                    pass
        elif len(diff_ori) > 1:
            print diff_ori[-1]+20
            if diff_ori[-1]+100 < Arr_target_len:
                timestamp_diff = (m[0] - Arr_target[j][0] for j in xrange(diff_ori[-1],diff_ori[-1]+100))
                for z in timestamp_diff:
                    if z >= 0:
                        ori_plus.append(z)
                    else:
                        ori_minus.append(z)
                if min(ori_plus) >= abs(max(ori_minus)):
                    if abs(max(ori_minus)) <= 0.05:
                        target_element = m[0] - max(ori_minus)
                        #print target_element
                        time_diff.append(abs(max(ori_minus)))
                        target_ori = np.where(Arr_target == target_element)
                        #print target_ori
                        if len(target_ori[0]) == 1:
                            target_ori1 = target_ori[0][0]
                            diff_ori.append(int(target_ori1))
                            ori_list.append(Arr_target[target_ori1])
                            Arr_source_temp.append(m)
                        elif len(target_ori[0]) > 1:
                            for k in xrange(len(target_ori)):
                                target_ori1 = target_ori[0][k]
                                diff_ori.append(int(target_ori1))
                                if Arr_target[target_ori1][3] == 1:
                                    ori_list.append(Arr_target[target_ori1])
                                    Arr_source_temp.append(m)
                                else:
                                    pass
                        else:
                            print "Can't find value from file target"
                    else:
                        pass
                else:
                    if min(ori_plus) <= 0.05:
                        target_element = m[0] - min(ori_plus)
                        #print target_element
                        time_diff.append(min(ori_plus))
                        target_ori = np.where(Arr_target == target_element)
                        #print target_ori1
                        if len(target_ori[0]) == 1:
                            target_ori1 = target_ori[0][0]
                            diff_ori.append(int(target_ori1))
                            ori_list.append(Arr_target[target_ori1])
                            Arr_source_temp.append(m)
                        elif len(target_ori[0]) > 1:
                            for k in xrange(len(target_ori)):
                                target_ori1 = target_ori[0][k]
                                diff_ori.append(int(target_ori1))
                                if Arr_target[target_ori1][3] == 1:
                                    ori_list.append(Arr_target[target_ori1])
                                    Arr_source_temp.append(m)
                                else:
                                    pass
                        else:
                            print "Can't find value from file target"
                    else:
                        pass
    print m[0]
if __name__ == '__main__':
    t = time()
    timestamp_com()
    #print Arr_source_temp
    np.savetxt('source.csv', np.array(Arr_source_temp), delimiter=',')
    np.savetxt('target.csv', np.array(ori_list), delimiter=',')
    print len(Arr_source_temp)
    #print ori_list
    print len(ori_list)
    print "total run time:"
    print time()-t
