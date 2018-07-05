# -*- coding: utf-8 -*-
#
# @Date    : 2018/7/4
# @Author  : Bin LIN
# Copyright (c) 2017-2018 University of St. Andrews, UK. All rights reserved
#

import os
import nibabel as nib
import pandas as pd
import matplotlib.pyplot as plt

data_folder = ['MICCAI_BraTS_2018_Data_Training/HGG', 'MICCAI_BraTS_2018_Data_Training/LGG']


def load_path(folder):
    volumes = []
    for grade in folder:
        files = os.listdir(grade)
        for file in files:
            volume = os.listdir(os.path.join(grade, file))
            for data in volume:
                data_path = os.path.join(grade, file, data)
                volumes.append(data_path)
    return volumes


whole_volumes = load_path(data_folder)

seg = []
flair = []
t1 = []
t1ce = []
t2 = []
scans = []
scans_dic = {}
for v in whole_volumes:
    if 'seg.nii' not in v:
        scans.append(v)
    if 'seg.nii' in v:
        seg.append(v)
    elif 'flair.nii' in v:
        flair.append(v)
    elif 't1.nii' in v:
        t1.append(v)
    elif 't1ce.nii' in v:
        t1ce.append(v)
    elif 't2.nii' in v:
        t2.append(v)
for s in seg:
    scans_dic[s] = []
    for scan in scans:
        if s[:-11] in scan:
            scans_dic[s].append(scan)

print(scans_dic)
print(len(scans_dic))

core = nib.load(t1ce[0])
tumor = core.get_data()
for a in tumor:
    plt.imshow(a,cmap='gray')
    plt.show()
exit(0)
gt = []
for key in scans_dic:
    d = nib.load(key)
    sc = d.get_data()
    gt.append(sc)
