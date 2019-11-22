import pyrsrc

data = pyrsrc.getStorage()

print "[DICT object]"
print data;

print ""

print "[Access Elements]"
print "STORAGE TOTAL: "+data['STORAGE_TOTAL']
print "STORAGE USAGE: "+data['STORAGE_USAGE']
print "STORAGE FREE: "+data['STORAGE_FREE']