import pyrsrc

data = pyrsrc.getRunning()

print "[DICT object]"
print data;

print ""

print "[Access Elements]"
print "RUNNING TIME: "+data['RUNNING_TIME']