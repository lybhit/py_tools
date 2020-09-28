#!/bash/bin/python
import sys
import time
import psutil

# get pid from args
if len(sys.argv) < 2:
	print ("missing pid arg")
	sys.exit()

# get process
pid = int(sys.argv[1])
p = psutil.Process(pid)

# monitor process and write data to file
interval = 1 # polling seconds
with open("process_monitor_" + p.name() + '_' + str(pid) + ".csv", "a+") as f:
	f.write("time,cpu%,mem%\n") # titles
	while True:
		current_time = time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))
		cpu_percent = p.cpu_percent()
		mem_percent = p.memory_percent()
		line = current_time + ',' + str(cpu_percent) + ',' + str(mem_percent)
		print (line)
		f.write(line + "\n")
		time.sleep(interval)