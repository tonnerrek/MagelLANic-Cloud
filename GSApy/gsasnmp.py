#!/usr/bin/python

from gsaerr import msgCLR, errMSG

try:
   import pysnmp
except ImportError:
   errMSG("Warning", "PySNMP module not found, trying net-snmp-utils.", 'STD_WRN')
   import subprocess
   snmpUtils = ('snmpwalk', 'snmpget')
   proc = subprocess.Popen(['which'] + list(snmpUtils), stdout=subprocess.PIPE)
   cmd = proc.communicate()
   if len(cmd[0].strip().split('\n')) != len(snmpUtils):
      errMSG("Error", "Cannot locate all required net-snmp-utils.")
   else: snmpFallback = 1

def snmpInit():
   print "snmpInit - test"

if __name__ == '__main__':
   print msgCLR('red', "!THIS IS NOT STANDALONE SCRIPT!", 1)

