#Author -deepak
#mass check whether sites are up
#sites to be added line by line in sites.txt
#requirement -- sites.txt

import httplib
import socket
import sys

print '-------------Start----------------------'
def check(choice):
  try:
      sitename = choice.strip()
      conn = httplib.HTTPConnection(sitename,80)
      ipaddr = socket.gethostbyname(sitename)
      conn.request("HEAD", "/")
      r1 = conn.getresponse()
      print " ********************* "
      print 'for -> ' + sitename
      print r1.status,r1.reason
      print 'IP address ->' + ipaddr
  except (KeyboardInterrupt, SystemExit):
      print '*********************ABORTING*******************'
      sys.exit()
  except:
      print '*********'
      print 'for -> ' + choice.strip() + ' Error -- Unreachable or incorrect domain'


for line in open('sites.txt','r').readlines():
    check(line)
print '-----------------END-----------------'

