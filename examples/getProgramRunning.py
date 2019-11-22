import pyrsrc

pid_file = "sample_pid.log"
data = pyrsrc.isProgramRunning(pid_file)

print "[DICT object]"
print data;

print ""

print "[Access Elements]"
print "PROGRAM CHECK: "+data['PROGRAM_CHECK']