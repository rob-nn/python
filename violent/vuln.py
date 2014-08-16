import socket
import sys

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(1)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except:
		return


def checkVulns(banner):
	if len(sys.argv)==2:
		filename = sys.argv[1]
		print '[+] Reading Vulnerabilities From: ' + filename
	f = open(filename, 'r')
	for line in f.readlines():
		if line.strip('\n') in banner:
			print "[+] Server is vulnerable: " + banner.strip('\n')
			

def main():
	portList = [21, 22]
	for x in range(1, 255):
		print x
		ip = '172.22.0.' + str(x)
		for port in portList:
			banner = retBanner(ip, port)
			if banner:
				print '[+] ' + ip + ': ' + banner
				#checkVulns(banner)

if __name__ == '__main__':
	main()
