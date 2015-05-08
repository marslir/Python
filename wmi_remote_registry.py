import wmi
import _winreg
#建立连接
c=wmi.WMI(computer="172.20.10.2",user="LIR",password="940914").StdRegProv
#查询键值
results,names = c.GetStringValue(hDefKey=2147483649,sSubKeyName=r"Software\\360desktop",sValueName="appinstall1")#r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\WindowsUpdate\\Auto Update\\Results\\Install",sValueName="LastSuccessTime")
#输出结果
print names
