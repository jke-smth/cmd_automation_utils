import subprocess
import time
for i in range(5):
	try:
		out_str = subprocess.check_output(["curl", "-Is", "https://jamex.captureitmedia.com/"], stderr=subprocess.STDOUT, encoding="UTF8")
		if "200 OK" in out_str:
			print("OK!")
		else:
			print("NOT OK! Check video website")
	except Exception as e:
		print(e)
	time.sleep(600)






