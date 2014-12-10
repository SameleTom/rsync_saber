#!/bin/env python
#-*- coding: utf-8 -*-
import os,sys

def scan(ips,port,userpass):
	f=open('/root/Desktop/result.txt','a+')
	for ip in ips:
		print ip
		isok = 0
		cmd = 'rsync %s:: --port=%s --timeout=5 --contimeout=2' % (ip,port)
		dirs = []
		for line in os.popen(cmd):
			line = line.strip().split(' ')[-1]
			isok = 1
			if line != '.':
				dirs.append(line)
		if isok:
			f.write(ip+'||'+port+'||root without pass'+'\n')
			print ip+'||'+port+'||root without pass'
		if len(dirs) > 0:
			for pwd in userpass:
				readok = 0
				os.system('echo '+pwd+' > /root/Desktop/pwd.txt')
				os.system('chmod 600 /root/Desktop/pwd.txt')
				the_dir = dirs[1]
				for user in ['','root','master']:
					cmd = 'rsync %s@%s::%s --port=%s --password-file="/root/Desktop/pwd.txt" --timeout=5 --contimeout=2' %(user,ip,the_dir,port)
					if os.popen(cmd).read():
						f.write(ip+'||'+port+'||'+pwd+'\n')
						print ip+'||'+port+'||'+pwd
						readok = 1
						break
				if readok:
					break
	f.close()

if __name__ == '__main__':
	port = raw_input('the port is ? : ')
	try:
		if str(int(port)) == port:
			port = port
		else:
			print 'some error and port is set to 873!'
			port = '873'
	except:
		print 'integer only and port is set to 873!'
		port = '873'
	ff = open('/root/Desktop/ip.txt')
	ips = []
	for ip in ff.readlines():
		ips.append(ip.strip())
	
	userpass = ['','111111','123456']
	
	print 'check start ...'
	scan(ips,port,userpass)
