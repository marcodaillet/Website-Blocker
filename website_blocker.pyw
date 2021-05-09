import time
from datetime import datetime as dt

# Change the hosts_path to /etc/hosts if you're on Mac or Linux
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com", "facebook.com"]

while True:
	# In the if just under this comment is the time condition you want the website blocker to work
	if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,19):
		with open(hosts_path, 'r+') as file:
			content=file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect + " " + website + "\n")
	else:
		with open(hosts_path, 'r+') as file:
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()
	time.sleep(5)