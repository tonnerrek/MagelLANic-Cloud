#!/usr/bin/env python

from sys import exit

class MSGColor:
  #only for 16color terminals
  map = {'black': '0m', 'red': '1m', 'green': '2m', 'yellow': '3m',
         'blue': '4m', 'magenta': '5m', 'cyan': '6m', 'gray': '7m'}
  bold  = '1;'
  lit   = '9'
  dim   = '3'
  clr   = '\33[0m'

def msgCLR(colorid, txt, enlight=0, bold=0):
   stx = '\33['
   if bold != 0:
      stx += MSGColor.bold
   if enlight == 0:
      stx += MSGColor.lit+MSGColor.map[str(colorid)]
   else:
      stx += MSGColor.dim+MSGColor.map[str(colorid)]
   return stx+txt+MSGColor.clr

def errMSG(header, message, type='STD_ERR', var=''):
   if type not in ('STD_ERR', 'VAR_ERR', 'STD_WRN'): raise ValueError("Bad message type in function errmsg ("+__name__+".py)")
   if type == 'STD_ERR':
      print msgCLR('red', "[ "+str(header)+" ] ", 1) + msgCLR('black', str(message))
   if type == 'VAR_ERR':
      print msgCLR('red', "[ "+str(header)+" ] ", 1) + msgCLR('black', str(message)) + msgCLR('yellow', str(var))
   if type == 'STD_WRN':
      print msgCLR('yellow', "[ "+str(header)+" ] ", 1) + msgCLR('black', str(message))
      return
   exit()

if __name__ == '__main__':
   print msgCLR('red', "!THIS IS NOT STANDALONE SCRIPT!", 1)
