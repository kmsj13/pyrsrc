import pyrsrc

data = pyrsrc.getRam()

print "[DICT object]"
print data;

print ""

print "[Access Elements]"
print "MEMORY TOTAL: "+data['MEM_TOTAL']
print "MEMORY USAGE: "+data['MEM_USAGE']
print "MEMORY FREE: "+data['MEM_FREE']