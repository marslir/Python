import wmi
#建立连接
c=wmi.WMI(computer="172.20.10.2",user="LIR",password="940914").StdRegProv
#查询键值，以下是hDefKey对应的值
#HKEY_CLASSES_ROOT (2147483648 (0x80000000))
#HKEY_CURRENT_USER (2147483649 (0x80000001))
#HKEY_LOCAL_MACHINE (2147483650 (0x80000002))
#HKEY_USERS (2147483651 (0x80000003))
#HKEY_CURRENT_CONFIG (2147483653 (0x80000005))
results,names = c.GetStringValue(hDefKey=2147483649,sSubKeyName=r"Software\\360desktop",sValueName="appinstall1")#r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\WindowsUpdate\\Auto Update\\Results\\Install",sValueName="LastSuccessTime")
#输出结果
print names
