import pyrsrc

data = pyrsrc.getTemp()

print "[DICT object]"
print data;

print ""

print "[Access Elements]"
print "TEMPERATURE: "+data['TEMPERATURE']