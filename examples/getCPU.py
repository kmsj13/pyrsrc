import pyrsrc

data = pyrsrc.getCPU()

print "[DICT object]"
print data;

print ""

print "[Access Elements]"
print "CPU USAGE: "+data['CPU_USAGE']
print "CPU FREE: "+data['CPU_FREE']