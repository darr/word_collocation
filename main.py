#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-08-06 17:15
# Modified date : 2019-08-06 17:16
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from collection_mi import MI_Train

#测试
def run():
    filepath = './data/data.txt'
    mipath = './data/result.txt'
    window_size = 5
    mier = MI_Train(window_size, filepath, mipath)
    mier.mi_main()

if __name__=='__main__':
    run()
