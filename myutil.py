#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zzx
# @Date:   2018-12-13 18:50:04
# @Last Modified by:   anchen
# @Last Modified time: 2018-12-13 19:33:08
#
# MIT License
# 
# Copyright (c) 2016 David Sandberg
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import os, glob
import random
import time
import cv2
import pandas as pd
import json
import pickle
import matplotlib.pyplot as plt

def plt_img(img, mode=None):
    if mode=='BGR':
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show() 

    
def sav_img(imgSavPath, img):
#support chinese path
#auto make dirs   
    savDir, savName = os.path.split(imgSavPath)
    imgType = savName.split('.')[1]
    if not os.path.exists(savDir):
        os.makedirs(savDir)
    cv2.imencode('.'+imgType, img)[1].tofile(imgSavPath)
    return


def print_ing(i, totalNum, stepNum=10, printStr='ing...'):
    if i+1<totalNum :
        if int(i%stepNum)==0:
            print(printStr+' %d/%d'%(i+1, totalNum), end='\r')
    else:
        print(printStr+' %d/%d'%(i+1,totalNum))
    return
