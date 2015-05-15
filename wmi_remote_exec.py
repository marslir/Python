import xlrd
import os
import wmi
fname = "hostlist.xlsx"
workbook = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
