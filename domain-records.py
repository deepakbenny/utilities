#author -deepak
#requires all sites in sites.txt
#dig command to list of sites


import socket
import dns.resolver



def resolve_query(site, query):
  try:
    answer = dns.resolver.query(site,query)
    print "For -> " + site
    for record in answer:
      print record.to_text()
  except (KeyboardInterrupt, SystemExit):
    print "-----------ABORTING------------"
  except:
    print "Error - "
    print '-------------------'


def init_func():
  print "yo"
  print "REQUIREMENT: sites.txt file in same dir, domains listed line by line"
  option = raw_input("Enter record you want to query(A|NS|MX|TXT): ")
  option_strip = option.strip().upper()

  for line in open('sites.txt','r').readlines():
     line_strip = line.strip()
     print '---------------'
     resolve_query(line_strip,option_strip)

init_func()
