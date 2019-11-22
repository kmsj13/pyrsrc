import pyrsrc

if __name__ == "__main__":
	
	CPU = pyrsrc.getCPU();
	RAM = pyrsrc.getRam();
	STORAGE = pyrsrc.getStorage();
	UPTIME = pyrsrc.getRunning();
	TEMPERATURE = pyrsrc.getTemp();
	
	print "[CPU USAGE]"
	print CPU;
	print ""

	print "[MEMORY USAGE]"
	print RAM;
	print ""

	print "[STORAGE USAGE]"
	print STORAGE;
	print ""

	print "[SYSTEM UPTIME]"
	print UPTIME;
	print ""

	print "[SYSTEM TEMPERATURE]"
	print TEMPERATURE;
	print ""

	