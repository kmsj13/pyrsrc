import json
import subprocess
import os, time



def getCPU():
	data = {};
	CPU_Pct=(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))
	data['CPU_USAGE'] = str(CPU_Pct) + "%"
	data['CPU_FREE'] = str(100-CPU_Pct) + "%"
	return data;
def display(val):
	return round(float(val),2)


def getRam():
	
	ramTotalGB = round(display(subprocess.check_output("free | awk 'FNR == 2 {print $2/1000000}'", shell=True)))
	Usage = subprocess.check_output("free | awk 'FNR == 2 {print $3/($2)*100}'", shell=True)
	
	data = {};
	data['MEM_TOTAL'] = str(ramTotalGB) + "GB"
	data['MEM_USAGE'] = str(display(Usage)) + "%"
	data['MEM_FREE'] = str(100 - display(Usage)) + "%"
	return data;

def getStorage():
	
	storageTotal = subprocess.check_output("df -h --total | awk  '/^total/ {print $2}'", shell=True).rstrip()
	storageUsed = subprocess.check_output("df -h --total | awk  '/^total/ {print $3}'", shell=True).rstrip()
	storageFree = subprocess.check_output("df -h --total | awk  '/^total/ {print $4}'", shell=True).rstrip()
	
	
	data = {};
	data['STORAGE_TOTAL'] = str(storageTotal)
	data['STORAGE_FREE'] = str(storageFree)
	data['STORAGE_USAGE'] = str(storageUsed)
	return data;

def getRunning():
	runningTime = subprocess.check_output("cat /proc/uptime | awk '{print $1}'", shell=True).rstrip()
	data = {};
	data['RUNNING_TIME'] = str(round(display(runningTime)/60/60,2))+"Hours"
	
	return data;

def getTemp():
	thermal = subprocess.check_output("cat /sys/class/thermal/thermal_zone0/temp", shell=True).rstrip()
	data = {};
	data['TEMPERATURE'] = str(round(float(thermal)/1000,2)) +"C"
	return data;	

def isProgramRunning(pid_file):
	Usage = subprocess.check_output("ps up `cat "+pid_file+"` >/dev/null && echo 'Running' || echo 'Not running'", shell=True)
	data = {};
	data['PROGRAM_CHECK'] = Usage
	#print Usage
	return data;

