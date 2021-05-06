# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:49:33 2021

@author: Inés Barbero
"""
import matplotlib.pyplot as plt 

hough_file='outlines.dat'
h_f = open(hough_file, 'r')
lines = h_f.readlines()
l1 = lines[0]
xmin = float(l1.split()[0])
xmax = float(l1.split()[1])
ymin = float(l1.split()[2])
ymax = float(l1.split()[3])
zmin = float(l1.split()[4])
zmax = float(l1.split()[5])

l2 = lines[1]
t0 = float(l2.split()[0])
t1 = float(l2.split()[1])

with open(hough_file, 'r') as f:
    lines = f.readlines()[2:]
    j=0
    for line in lines:
        x=[]
        y=[]
        ax = float(line.split()[0])
        bx = float(line.split()[3])
        ay = float(line.split()[1])
        by = float(line.split()[4])
        az = float(line.split()[2])
        bz = float(line.split()[5])
        
        #Choose combination of axis...
        # plt.plot([ax+t0*bx,ax+t1*bx],[ay+t0*by,ay+t1*by])
        # plt.xlim([xmin, xmax])
        # plt.ylim([ymin, ymax])
        plt.plot([ay+t0*by,ay+t1*by],[az+t0*bz,az+t1*bz])
        plt.xlim([ymin, ymax])
        plt.ylim([zmin, zmax])
        # plt.plot([ax+t0*bx,ax+t1*bx],[az+t0*bz,az+t1*bz])
        # plt.xlim([xmin, xmax])
        # plt.ylim([zmin, zmax])
    
    