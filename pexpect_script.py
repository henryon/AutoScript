#!/usr/bin/env python


#-*-coding:UTF-8 -*-

log_dir='/opt/path/logs/'

client_tmp_dir='/opt/path/tmp'

sshd_port='22'

script_dir='/opt/path/script'

node_list=[{'ip':'192.168.1.1','user':'root','password','123456','cmd':'sh /script.sh'},
 {'ip':'192.168.1.2', 'user':'root', 'passwd':'123456', 'cmd':'sh /tmp/dpkg_client_ubuntu_x.x86_64.sh'} ]


 #!/usr/bin/env python

 #-*- coding:UTF-8 -*-

 import os
 import sys
 import platform
 import conf
 import subprocess


 Class Server:
 	def GetOS(self):
 		Branch=platform.dist()[0]
 		return Branch
 	def GetRelease(self):
 		Release=platform.dist()[1]
 		return Release
 	def GetInstaller(self):
 		if self.GetOS() in ['Ubuntu','debian']:
 			installer='apt-get'
 		elif self.GetOS() in ['redhat','fedora','centos']:
 			installer='yum'
 		elif self.GetOS() in ['Suse']:
 			installer='zypper'
 		else:
 			installer='unknown'
 		return installer

 try:
 	import pexpect
 except ImportError:
 	install=Server()
 	inst=install.GetInstaller()
 	if (inst =='apt-get') or (inst == 'zypper'):
 		cmd= '%s install python-pexpect' % (intst)
 	elif inst == 'yum':
 	    cmd= '%s install pexpect ' % (inst)
 	else:
 		cmd= 'echo "Not support yet:"'
 try:
 	fd=subprocess.Popen(cmd,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 	out=fd.stdout.readlines()
 	err=fd.stderr.readlines()
 	all= out+err
 	all=''.join(all)
 except OSError,e:
 	all="Cannot run command,Exception:" + e +os.linesep
 import pexect

 Class Except():
 	def ssh(self,ip,port,user,passwd,cmd):
 		ssh=pexpect.spawn('ssh -p %s %s@%s' % (port,user,ip,cmd))
 		r=''
 	try:
 		i=ssh.expect(['password:','continue connecting(yes/no)?'],timeout=5)
 		if i == 0:
 			ssh.sendline(passwd)
 		elif i == 1:
 			ssh.sendline('yes')
 			ssh.expect('password:')
 			sshd.sendline(passwd)
 	expect pexpect.EOF:
 		ssh.close()
 		else:
 			r=ssh.read()
 			ssh.expect(pexpect.EOF)
 			ssh.close()
 		return r

 	def scp(self,ip,port,user,passwd,srcfile='index.html',distpath):
 		ssh=pexpect.spawn('scp -P %s %s %s@%s:%s' % (port,file,user,ip,distpath))
 		r=''
 		try:
 			i=ssh.expect(['password:','continue connecting(yes/no)?'],timeout=5)
 		if i == 0:
 			ssh.sendline(passwd)
 		elif i == 1:
 			ssh.sendline('yes')
 			ssh.expect('password:')
 			ssh..sendline(passwd)
 		except pexpect.EOF:
 			ssh.close()
 		else:
 			r=ssh.read()
 			ssh.expect([pexpect.EOF])
 			ssh.close()
 		return r

 packages=conf.package_dir
 logs=conf.log_dir
 c_tmp=conf.client_tmp_dir
 port=conf.sshd_port
 scripts=conf.script_dir
 nodes=conf.node_list

 os.system('sh'+scripts+"dpkg_server_x64.sh")

 for i in range(len(nodes)):
 	ip=nodes[i]['ip']
 	user=nodes[i]['user']
 	passwd=nodes[i]['passwd']
 	cmd=nodes[i]['cmd']
 r=expect.scp(ip,port,user,passwd,script+
 script_name',c_tmp)
 print r
 r=expect.sshd(ip,port,user,passwo,cmd)
 print r


 