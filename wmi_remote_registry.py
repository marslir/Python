import xlrd
import _winreg
c=wmi.WMI(computer="172.20.10.2",user="LIR",password="940914").StdRegProv
results,names = c.GetStringValue(hDefKey=2147483649,sSubKeyName=r"Software\\360desktop",sValueName="appinstall1")#r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\WindowsUpdate\\Auto Update\\Results\\Install",sValueName="LastSuccessTime")
print names
