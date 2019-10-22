#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   hshi
#   E-mail  :   snapwings3190@163.com
#   Date    :   19/10/09 18:43:53
#   Desc    :   
from time import time
import os
import numpy as np
import my_func

if __name__ == '__main__':
    t = time()
    print os.getcwd()
    my_func.timestamp_com(os.getcwd()+'/ub482_ego.csv', os.getcwd()+'/ub482_target.csv')
    final_target = np.delete((np.array(my_func.ori_list)), 0, axis=1)
    final_arr = np.concatenate(((np.array(my_func.Arr_source_temp)), final_target), axis=1)
    np.savetxt('position_vel.csv', final_arr, delimiter=',')
    print len(my_func.Arr_source_temp)
    print len(my_func.ori_list)
    print "total run time:"
    print time()-t


