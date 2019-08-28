#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   hshi
#   E-mail  :   snapwings3190@163.com
#   Date    :   19/08/24 17:27:10
#   Desc    :   

import numpy as np

time1 = np.loadtxt('time_stamp.txt')

time2 = np.loadtxt('log_adas_client_log20190820-145516.7818_time1')

len_time1 = len(time1)
len_time2 = len(time2)

try:
    len(time1) == len(time2)
except:
    print "Please check the time_stamp.txt's lines"
#print time2
merge_time = []
i = 0
while i < len_time1:
    merge_time0 = float(time1[0]) + float(time2[i][0]/1000000)
    merge_time.append(merge_time0)
    i += 1
#print merge_time
#print len(merge_time)
time2_1 =np.delete(time2, 0, axis=1)
merge_time1 = np.array(merge_time)
#print merge_time1
#print merge_time1.shape
merge_time2 = merge_time1.reshape(-1, 1)
#print merge_time2
#print "==========="
#print time2_1
#print time2_1.shape
log_time = np.concatenate((merge_time2,time2_1), axis=1)
#print log_time
np.savetxt('log_merge.csv', log_time, delimiter=',', header="time_stamp, fps, cpu, mem, delay")

