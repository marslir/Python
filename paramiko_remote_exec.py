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
  computer = sh.cell_value(i,0)
  user = sh.cell_value(i,1)
  password = sh.cell_value(i,2)
  try:
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(computer,22,user,password,timeout=5)
    f.write("IP " + computer + "connected\n")
    fcmd = open("./cmd/command.txt" , "r")
    for line in fcmd:
      f.write(line.replace('\n','')+"\n")
      stdin,stdout,stderr = ssh.exec_command(line.replcae('\n',''))
      out=stdout.read()
      f.write(out)
    fcmd.close()
  except Exception, e:
    f.write("connection to " + computer + "failed\n")
    continue
  ssh.close
f.close()
