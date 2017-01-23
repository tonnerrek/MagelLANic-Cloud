#!/usr/bin/env python

import sys, re
import curses
#gsa specific modules
from gsaerr import errMSG
from gsasnmp import snmpInit as test
import crypto

cc = ('WW', 'AF', 'EG', 'DZ', 'AR', 'ET', 'AU', 'BH', 'BD', 'BE', 'BA', 'BR', 'BG', 'CL', 'CN', 'DK', 'DE',
      'EC', 'EE', 'FI', 'FR', 'GE', 'GR', 'GB', 'GT', 'HK', 'IN', 'ID', 'IQ', 'IE', 'IL', 'IT', 'JP', 'YE',
      'JO', 'CM', 'CA', 'KZ', 'QA', 'KE', 'CO', 'KR', 'HR', 'LB', 'LY', 'LU', 'MY', 'MT', 'MA', 'MX', 'MZ',
      'NZ', 'NL', 'NO', 'OM', 'AT', 'PK', 'PH', 'PL', 'PT', 'PR', 'RO', 'RU', 'SA', 'SE', 'CH', 'CS', 'SG',
      'SK', 'SI', 'ES', 'ZA', 'SD', 'SY', 'TW', 'TH', 'CZ', 'TN', 'TR', 'UA', 'HU', 'US', 'UZ', 'AE', 'VN')
vlan = {'name': "", 'id': 0, 'domain': ""}

def inputCheck(vname, vid, mgmtdomain, strict=1):
##VLAN_ID
   if vid <= 1 or vid > 4094:
      errMSG("Error", "VLAN ID value is incorrect or restricted: "+str(vid))
##MGMT_DOMAIN
   if not re.match("^SAG [A-Z]{2} [A-Z0-9 ]+$", mgmtdomain):
      errMSG("Error", "Management domain is incorrect: ", "VAR_ERR", mgmtdomain)
   if mgmtdomain[4:6] not in cc:
      errMSG("Error", "Unrecongnised contry code: ", "VAR_ERR", mgmtdomain[4:6])
##VLAN_NAME
   if not re.match("^[A-Za-z0-9_\-:\.]+$", vname):
      errMSG("Error", "VLAN Name is incorrect: ", "VAR_ERR", vname)
   if not re.match("^VL\-G\-[A-Z]{2}\-[A-Z]{2}[0-9]{2}\-[0-9]{4}$", vname) and strict == 1:
      errMSG("Error", "VLAN Name is not GAIN complaint: ", "VAR_ERR", vname)
   if vname[5:7] != mgmtdomain[4:6] and strict == 1:
      errMSG("Error", "VLAN Name and domain have different country codes: ", "VAR_ERR", vname[5:7]+" != "+mgmtdomain[4:6])

if __name__ == '__main__':
   if len(sys.argv[1:]) < 1:
      errMSG("Error", "No arguments provided while running as main.")
   if len(sys.argv[1:]) < 3:
      errMSG("Error", "Not enought arguments.")
   vlan['id'] = int(sys.argv[1])
   vlan['name'] = sys.argv[3]
   vlan['domain'] = sys.argv[2]

   inputCheck(vlan['name'], vlan['id'], vlan['domain'])
   test()
