import json
import subprocess
import os, time

data = {};

def getCPU():
	CPU_Pct=(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))

	global data;
	data['CPU_USAGE'] = str(CPU_Pct) + "%"

def display(val):
	return round(float(val),2)


def getRam():
	
	ramTotalGB = round(display(subprocess.check_output("free | awk 'FNR == 2 {print $2/1000000}'", shell=True)))
	Usage = subprocess.check_output("free | awk 'FNR == 2 {print $3/($2)*100}'", shell=True)
	
	
	global data;
	data['MEM_TOTAL'] = str(ramTotalGB) + "GB"
	data['MEM_USAGE'] = str(display(Usage)) + "%"
	data['MEM_FREE'] = str(100 - display(Usage)) + "%"


def getStorage():
	
	storageTotal = subprocess.check_output("df -h --total | awk  '/^total/ {print $2}'", shell=True).rstrip()
	storageUsed = subprocess.check_output("df -h --total | awk  '/^total/ {print $3}'", shell=True).rstrip()
	storageFree = subprocess.check_output("df -h --total | awk  '/^total/ {print $4}'", shell=True).rstrip()
	
	
	global data;
	data['STORAGE_TOTAL'] = str(storageTotal)
	data['STORAGE_FREE'] = str(storageFree)
	data['STORAGE_USAGE'] = str(storageUsed)
	

def getSys():
	runningTime = subprocess.check_output("cat /proc/uptime | awk '{print $1}'", shell=True).rstrip()
	thermal = subprocess.check_output("cat /sys/class/thermal/thermal_zone0/temp", shell=True).rstrip()

	
	global data;
	data['RUNNING_TIME'] = str(round(display(runningTime)/60/60,2))+"Hours"
	data['TEMPERATURE'] = str(round(float(thermal)/1000,2)) +"C"

def isProgramRunning(pid_file):
	Usage = subprocess.check_output("ps up `cat "+pid_file+"` >/dev/null && echo 'Running' || echo 'Not running'", shell=True)
	global data;
	data['PROGRAM_CHECK'] = Usage
	#print Usage


if __name__ == "__main__":
	getCPU();
	getRam();
	getStorage();
	getSys();
	#isProgramRunning("/opt/pid.log");

	print "CPU USAGE:\t" + data['CPU_USAGE'];
	print "MEMORY TOTAL:\t" + data['MEM_TOTAL'];
	print "MEMORY USAGE:\t" + data['MEM_USAGE'];
	print "MEMORY FREE:\t" + data['MEM_FREE'];
	print "STORAGE TOTAL:\t" + data['STORAGE_TOTAL'];
	print "STORAGE USAGE:\t" + data['STORAGE_USAGE'];
	print "STORAGE FREE:\t" + data['STORAGE_FREE'];
	print "RUNNING TIME:\t" + data['RUNNING_TIME'];
	print "CPU TEMP:\t" + data['TEMPERATURE'];
	#print "IS PROGRAM RUNNING:\t" + data['PROGRAM_CHECK'];
	
	#print in JSON
	#print data