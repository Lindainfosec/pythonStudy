#coding:utf-8
import ftplib
#ftp server ip uname pwd
ip = '192.168.1.103'
port = 21
uname = 'test1'
pwd = 'abc123'

#ftp connect & login
def ftp_init():
	ftp = ftplib.FTP()
	print (ftp.connect(ip, port))
	print (ftp.login(uname, pwd))
	return ftp

def ftp_callback(buf):
	print (buf)

#download ftp server -> local
def ftp_download(ftp, remote_dir, remote_file, local_file):
	print (ftp.cwd(remote_dir))
	f = open(local_file, 'wb')
	ftp.retrbinary('RETR %s'%remote_file, f.write)  #断点续传
	f.close()

#upload local -> ftp server
def ftp_upload(ftp, remote_dir, remote_file, local_file):
	print (ftp.cwd(remote_dir))
	f = open(local_file, 'rb')
	ftp.storbinary('STOR %s'%remote_file, f)
	f.close()

def ftp_exit(ftp):
	ftp.close()

if __name__ == '__main__':
	#ftp server dir file
	aim_dir = 'ftp_dir'
	#aim_file = '1.txt'
	
	#save local file
	#download_fname = r'C:\Users\hyg\Desktop\ftp\download.txt'
	#upload_fname = r'C:\Users\hyg\Desktop\ftp\song.txt'
	#ftp = ftp_init()
	#ftp_download(ftp, aim_dir, aim_file, download_fname)
	#ftp_exit(ftp)
	
	#ftp = ftp_init()
	#ftp_upload(ftp, aim_dir, 'song.txt', upload_fname)
	#ftp_exit(ftp)
	ftp = ftp_init()
	ftp.dir()
