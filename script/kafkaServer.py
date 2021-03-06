#!/bin/python
from __future__ import print_function
import subprocess
import sys
import os
import json
from util import appendline, get_ip_address


if __name__ == "__main__":
	# start server one by one
	if len(sys.argv) < 2 or sys.argv[1] not in ['start', 'stop']:
		sys.stderr.write("Usage: python %s start or stop\n" % (sys.argv[0]))
		sys.exit(1)
	else:
		path = os.path.dirname(os.path.realpath(__file__))
		config = json.load(open(path+'/cluster-config.json'))
		if sys.argv[1] == 'start':
			for node in config['nodes']:
				if node['kafka']:
					subprocess.Popen(['ssh', 'cloud-user@'+node['ip'], 'nohup bash /usr/local/kafka/bin/kafka-server-start.sh /usr/local/kafka/config/server.properties&'])
		else:
			for node in config['nodes']:
				if node['kafka']:
					subprocess.Popen(['ssh', 'cloud-user@'+node['ip'], 'bash /usr/local/kafka/bin/kafka-server-stop.sh'])
