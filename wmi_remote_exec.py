import xlrd
import os
import wmi
fname = "hostlist.xlsx"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
  sh = wb.sheet_by_name("Sheet1")
except:
  print "no sheet in %s named Sheet1" % fname
nrows = sh.nrows
ncols = sh.ncols
f = open("./log/checklog.log","a")
for i in range(0,nrows):
  computer = sh.cell_value(i,0)
  user=sh.cell_value(i,1)
  password=sh.cell_value(i,2)
  try:
    conn = wmi.WMI(computer = computer, user = user ,password = password)
    f.write(computer+" connected\n")
  except:
    f.write(computer+" connection failed\n")
    continue
  try:
    process_id,return_value = conn.Win32_Process.Create(CommandLine="cmd /c net localgroup administrators hbpc_aqhc /add")
    f.write("users hbpc_aqhc added to administrators group\n")
  except:
    f.write("add hbpc_aqhc to administrators group failed\n")
f.close()
