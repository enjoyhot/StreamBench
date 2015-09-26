#!/bin/python
from __future__ import print_function
import subprocess
import json

if __name__ == "__main__":
	config = json.load(open('cluster-config.json'))
	# install git, clone repository, install jdk
	for node in config['nodes']:
		print("Install git on server %s" % node['ip'])
		# install git
		if '/usr/bin/git' not in subprocess.check_output(["ssh", "cloud-user@"+node['ip'], 'whereis git']):
			subprocess.call(["ssh", "cloud-user@"+node['ip'], "sudo apt-get install -y git"])
			print("Install git")
		# clone repository
		files = subprocess.check_output(["ssh", "cloud-user@"+node['ip'], 'ls /home/cloud-user'])
		if 'RealtimeStreamBenchmark' not in files:
			subprocess.call(["ssh", "cloud-user@"+node['ip'], "git clone https://github.com/wangyangjun/RealtimeStreamBenchmark.git"])
		else:
			subprocess.Popen('ssh cloud-user@'+node['ip']+'"cd /home/cloud-user/RealtimeStreamBenchmark;git pull;"', shell=True)

		# install jdk
		subprocess.call(["ssh", "cloud-user@"+node['ip'], "python /home/cloud-user/RealtimeStreamBenchmark/script/install-jdk.py"])

		# install storm
		subprocess.call(["ssh", "cloud-user@"+node['ip'], "python /home/cloud-user/RealtimeStreamBenchmark/script/install-storm.py"])

