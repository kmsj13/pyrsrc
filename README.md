# pyrsrc
Linux System Resource Monitoring via Python

```bash
Written by: 

Kevin San Jose
E-mail: kmsj13@gmail.com
Web: www.kmsj13.com

My Inspiration:
Jenny, Jervyna, Jazmin
```


## Install
```bash
$ git clone https://github.com/kmsj13/pyrsrc.git
$ cd pyrsrc
$ cd install
$ sudo python setup.py install
```

## Usage
```python
import pyrsrc
if __name__ == "__main__":
  CPU = pyrsrc.getCPU();

  RAM = pyrsrc.getRam();
  STORAGE = pyrsrc.getStorage();
  UPTIME = pyrsrc.getRunning();
  TEMPERATURE = pyrsrc.getTemp();

  print "[CPU USAGE]"
  print CPU;

  print "[MEMORY USAGE]"
  print RAM;

  print "[STORAGE USAGE]"
  print STORAGE;

  print "[SYSTEM UPTIME]"
  print UPTIME;

  print "[SYSTEM TEMPERATURE]"
  print TEMPERATURE;

```


## Functions
### getCPU()
Get CPU Usage.
```python
CPU = pyrsrc.getCPU()
print CPU['CPU_USAGE']
print CPU['CPU_FREE']
```

### getRam()
Get RAM Usage.
```python
RAM = pyrsrc.getRam()
print RAM['MEMORY_TOTAL']
print RAM['MEMORY_USAGE']
print RAM['MEMORY_FREE']
```
### getStorage()
Get Storage Usage.
```python
STORAGE = pyrsrc.getStorage()
print STORAGE['STORAGE_TOTAL']
print STORAGE['STORAGE_USAGE']
print STORAGE['STORAGE_FREE']
```

### getTemp()
Get CPU Temperature.
```python
CPUTEMP = pyrsrc.getTemp()
print CPUTEMP['TEMPERATURE']
```

### getRunning()
Get System Uptime.
```python
UPTIME = pyrsrc.getRunning()
print UPTIME['RUNNING_TIME']
```
### isProgramRunning(pid_file)
Check if certain PID is running.
pid_file = location of file where specific PID is written.

```python
pid_file = "sample_pid.log"
CHECK = pyrsrc.isProgramRunning(pid_file)
print CHECK['PROGRAM_CHECK']
```

## Future Plan
1. Getting System Resource from Windows Machine
2. Creating a simple dashboard
