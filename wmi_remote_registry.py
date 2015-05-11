import xlrd
import os
import wmi
fname = "check.xlsx"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
  sh = bk.sheet_by_name("Sheet1")
except:
  print "no sheet in %s named Sheet1" % fname
nrows = sh.nrows
ncols = sh.ncols
for i in range(0,nrows):
  computer = sh.cell_value(i,0)
  user = sh.cell_value(i,1)
  password = sh.cell_value(i,2)
  f = open("./log/history.log", "a")
  conn=wmi.WMI(computer=computer,user=user,password=password,namespace="root/default").StdRegProv
  f.write("IP address " + computer + "connected\n")
  results,detect = conn.GetExpandedStringValue(hDefKey=2147483650,sSubKeyName=r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\WindowsUpdate\\Auto Update\\Results\\Detect",sValueName="LastSuccessTime")
  f.write("Last Detect Time :\n" + detect + "\n")
  results,download = conn.GetExpandedStringValue(hDefKey=2147483650,sSubKeyName=r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\WindowsUpdate\\Auto Update\\Results\\Detect",sValueName="LastSuccessTime")
  f.write("Last Detect Time :\n" + download + "\n")
  results,install = conn.GetExpandedStringValue(hDefKey=2147483650,sSubKeyName=r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\WindowsUpdate\\Auto Update\\Results\\Detect",sValueName="LastSuccessTime")
  f.write("Last Detect Time :\n" + install + "\n")
  timenow=time.strftime('%a,%d,%b,%Y,%H:%M:%S',time.localtime())
  f.wirte("Checked at local time:\n",timenow)
  
