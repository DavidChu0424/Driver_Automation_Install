# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 20:30:25 2021

@author: David_Chu
"""
import os
from os import listdir
from os.path import isfile, isdir, join
import sys

file_path = str(input("請輸入 Driver 路徑: "))              
files = os.listdir(file_path)
files.remove(os.path.basename(__file__))

def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text


def exportTxt(cmdresult, username):
    with open(username + "_Pass" + ".txt","w") as f:
      f.write(cmdresult)

    
for i in range(len(files)):
    cmd = str(files[i]) + "  /s"
    execCmd(cmd)
    

    
          

