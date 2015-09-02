#-*- coding:utf-8 -*-
import time
import datetime
import re
import subprocess
import sys
import wmi
import os
import ConfigParser
import _winreg
import win32net
import win32api
import win32con
import win32netcon
import win32security
c=wmi.WMI()
class myWMI(object):
    def __init__(self,wmiclass,info={},name=''):
        if name:
            self.obj = wmiclass(Name = name)
        else:
            self.obj = wmiclass()
        self.info = info
        return self.obj
class myAccount(myWMI):
    def __init__(self,name="",group=""):
        self.uname = name
        self.gname = group
        self.uobj=myWMI.__init__(self,c.Win32_UserAccount,name = self.uname)
        self.guoub = myWMI.__init__(self,c.Win32_GroupUser,name=self.gname)
    def show_user_list(self):
        ulist=[]
        for user in self.uobj:
            ulist.append(user.Name)
        return ulist
class myOs(object):
    def __init__(self,wmiobj=c,info={}):
        self.obj=wmiobj.Win32_OperatingSystem()[0]
        self.cobj=wmiobj.Win32_ComputerSystem()[0]
        self.disk_obj= wmiobj.Win32_DiskDrive()
        self.Partition_obj= wmiobj.Win32_LogicalDisk()
        self.networkAdapter_obj = wmiobj.Win32_NetworkAdapterConfiguration (IPEnabled=1)
        self.process_obj = wmiobj.Win32_Processor()[0]
        self.update_obj = wmiobj.Win32_QuickFixEngineering()
        self.info=info
    def get_os_info(self):
        self.info["os"]=self.obj.Caption
        self.info["version"]=self.obj.CSDVersion
        self.info["fullname"]=self.obj.CSName
        self.info["localtime"]=datetime.datetime.strptime(str(str(self.obj.LocalDateTime ).split('.')[0]),'%Y%m%d%H%M%S')
        self.info["lastboottime"]=datetime.datetime.strptime(str(str(self.obj.LastBootUpTime ).split('.')[0]),'%Y%m%d%H%M%S')
        self.info["os_architecture"]=self.obj.OSArchitecture
        self.info["mu_languages"]=self.obj.MUILanguages[0]
        self.info["SerialNumber"]=self.obj.SerialNumber
        self.info["cpu_count"]=self.cobj.NumberOfProcessors
        self.info["mainboard"]=self.cobj.Manufacturer
        self.info["board_model"]=self.cobj.Model
        self.info["systemtype"]=self.cobj.SystemType
        self.info["physical_memory"]=int(self.cobj.TotalPhysicalMemory)/1024/1024
        self.info["cpu_name"] = self.process_obj.Name
        self.info["clock_speed"] = self.process_obj.MaxClockSpeed
        self.info["number_core"] = self.process_obj.NumberOfCores
        self.info["data_width"] = self.process_obj.DataWidth
        self.info["socket_desigination"] = self.process_obj.SocketDesignation
        self.info["l2_cache"] = self.process_obj.L2CacheSize
        self.info["l3_cache"] = self.process_obj.L3CacheSize
        return self.info
    def update_infomation(self):
        for s in self.update_obj:
            print '%-10s %-10s %-20s %-10s\n' %(s.HotFixID,s.InstalledOn,s.Description,s.InstalledBy)   
class mySoft(myWMI):
    def __init__(self,name=""):
        self.name=name
        myWMI.__init__(self,c.Win32_Product,name=self.name)
    def get_software(self):
        softlist=[]
        for soft in self.obj:
            softlist.append((soft.Name,soft.InstallDate))
        return softlist
ulist = myAccount().show_user_list()
for i in ulist:
    print i
myOs().update_infomation()
softlist = mySoft().get_software()
for soft in softlist:
    print soft[0],'\n',soft[1]
osinfo = myOs().get_os_info()
print osinfo["cpu_name"]

