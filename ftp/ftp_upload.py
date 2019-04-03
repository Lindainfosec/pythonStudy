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
	f = open(local_file+'\\'+remote_file, 'wb')
	ftp.retrbinary('RETR %s'%remote_file, f.write)
	f.close()

#upload local -> ftp server
def ftp_upload(ftp,local_file):
	f = open(local_file, 'rb')
	ftp.storbinary('STOR %s'%local_file, f)
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
	os.mkdir(path)

	for _dir in tmp['dirs']:
		ftp_download_dir(ftp, _dir, path)

	for fname in tmp['files']:
		ftp_download(ftp, fname, path)
	ftp.cwd('..')

def get_local_dir(ftp, local_dir):
	print ('>>> dir:', local_dir)
	os.chdir(local_dir)
	ftp.mkd(local_dir)
	ftp.cwd(local_dir)
	files = os.listdir()
	for l in files:
		if os.path.isdir(l):
			get_local_dir(ftp, l)
		elif os.path.isfile(l):
			print ('file:', l)
			ftp_upload(ftp, l)
		else:
			print ('ignore', l)
	os.chdir('..')
	ftp.cwd('..')
	print ('<<< dir:', local_dir)

if __name__ == '__main__':
	#ftp server dir remote_file
	
	ftp = ftp_init()
	upload_rootdir = r'C:\Users\hyg\Desktop\ftp'
	upload_dir = 'test_dir'
	os.chdir(upload_rootdir)

	get_local_dir(ftp, upload_dir)