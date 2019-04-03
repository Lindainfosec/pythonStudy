#coding:utf-8
import ftplib
import os
#ftp server ip uname pwd
ip = '192.168.1.103'
port = 21
uname = 'test1'
pwd = 'abc123'

root_dir = r'C:\Users\hyg\Desktop\ftp'

remoteDirInfo = {}

#ftp connect & login
def ftp_init():
	ftp = ftplib.FTP()
	print (ftp.connect(ip, port))
	print (ftp.login(uname, pwd))
	return ftp

def ftp_callback(buf):
	print (buf)

#download ftp server -> local
def ftp_download(ftp, remote_file, local_file):
	fname = local_file+'\\'+remote_file
	lsize = 0
	if os.path.exists(fname):
		lsize = os.lstat(fname).st_size
	f = open(fname, 'ab')
	print ('lsize =', lsize)
	ftp.retrbinary('RETR %s'%remote_file, f.write, rest=lsize)
	f.close()

#upload local -> ftp server
def ftp_upload(ftp, remote_dir, remote_file, local_file):
	print (ftp.cwd(remote_dir))
	f = open(local_file, 'rb')
	ftp.storbinary('STOR %s'%remote_file, f)
	f.close()

def ftp_exit(ftp):
	ftp.close()

def ftp_get_dirinfo(line):
	result = line.split()
	f_type = result[0][0]
	if f_type == '-':
		key = 'files'
	elif f_type == 'd':
		key = 'dirs'
	else:
		return 
	remoteDirInfo[key].append(result[-1])
	
def ftp_download_dir(ftp, remotedir = '.', localdir = '.'):
	global remoteDirInfo
	ftp.cwd(remotedir)
	remoteDirInfo = {'parent':remotedir, 'dirs':[], 'files':[]}
	ftp.dir(ftp_get_dirinfo)
	tmp = remoteDirInfo
	print (tmp)

	path = localdir + '\\' + remotedir
	if not os.path.exists(path):
		os.mkdir(path)

	for _dir in tmp['dirs']:
		ftp_download_dir(ftp, _dir, path)

	for fname in tmp['files']:
		ftp_download(ftp, fname, path)
	ftp.cwd('..')


if __name__ == '__main__':
	#ftp server dir remote_file
	aim_dir = 'ftp_dir'
	ftp = ftp_init()	
	ftp_download_dir(ftp, aim_dir, root_dir)