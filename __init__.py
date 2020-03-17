'''
Created on Mar 2, 2017

@author: Krystal
'''
from tkinter import *
from main import *

import os, glob
import datetime


alphabet = "abcdefghijklmnopqrstuvwxyz"
numberS = ["1","2","3","4","5","6","7","8","9","0"]
shift = 1


list1=list("abcdefghijklmnopqrstuvwxyz")  
num=1 
list2 = []




PasswordLibrary = []

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
myfile_path = os.path.join(ROOT_PATH)

RecentActivity = open("RecentActivity.txt", "a")
PasswordLog = open("PasswordLog.txt", "a")






    
