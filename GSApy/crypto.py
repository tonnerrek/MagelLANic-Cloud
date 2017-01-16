#!/usr/bin/env python
#
# zvk@2017
# pseudo crypto module for Cisco and Juniper weak password
#

import gsaerr
from re import match
from random import randit

vig = (0x64,0x73,0x66,0x64,0x3b,0x6b,0x66,0x6f,0x41,0x2c,0x2e,0x69,0x79,0x65,0x77,0x72,0x6b,0x6c,0x64,0x4a,
       0x4b,0x44,0x48,0x53,0x55,0x42,0x73,0x67,0x76,0x63,0x61,0x36,0x39,0x38,0x33,0x34,0x6e,0x63,0x78,0x76,
       0x39,0x38,0x37,0x33,0x32,0x35,0x34,0x6b,0x3b,0x66,0x67,0x38,0x37);

def cisco7Decrypt(inputHash):
   output = None
   inputHash = inputHash.upper()

   if len(inputHash) %2 != 0 or not match('^[0-9]{2}[0-9A-F]{2,}$', inputHash):
      gsaerr.errMSG("WARNING", "Incorret Cisco type7 hash", 'STD_WRN')
   else:
      inputHash = [int(inputHash[i:i+2], 16) if i > 0 else int(inputHash[i:i+2]) for i in xrange(0, len(inputHash), 2) ]
      output = "".join([chr(i ^ vig[(inputHash[0] + id) % 53]) for id, i in enumerate(inputHash[1:])])
   return output

def cisco7Encrypt(inputString):
   seed = randint(0, 15)
   output = "{0:0>2}".format(seed) + "".join([format((ord(i) ^ vig[(seed + id) % 53]), '02X')  for id, i in enumerate(inputString)])
   return output

if __name__ == '__main__':
   pass
