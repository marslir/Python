import xlrd
import os
import paramiko
import time
fname = "list.xlsx"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
  sh = bk.sheet_by_name("Sheet1")
except:
  print "no sheet in %s named Sheet1" % fname
nrows = sh.nrows
ncols = sh.ncols
f = open("./log/history.log" , "a")
for i in range(0,nrows):
