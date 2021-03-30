chapter 6 -steps 

		Example 1
1. install nano, apache2, telnet> all installed by default. executed: sudo apt install update
	to be sure all wer updated.
2.Run telnet with correct arguments/parameters:telnet www.your-server.com 80
	curl GET/HTTP/1.1
3.HOST: HTTPS://www.amazom.com/title
	curl -xPut -d -"userid=5&title =PUT Title&Body =PUT-Content." http://www.amazon.com/title
install tcpflow 
	tcpflow -p -c -i eth0 port 80 | grep -oE '(GET|POST|HEAD) .* HTTP/1.[01]|Host: .*'
reportfilename: ./report.xml

		Example 2

amberlowe1001@DESKTOP-TV565H4:~$ sudo useradd -D
[sudo] password for amberlowe1001:
GROUP=100
HOME=/home
INACTIVE=-1
EXPIRE=
SHELL=/bin/sh
SKEL=/etc/skel
CREATE_MAIL_SPOOL=no
amberlowe1001@DESKTOP-TV565H4:~$

added user "devops_1" to admin
	 sudo adduser devops_1 admin
Adding user `devops_1' to group `admin' ...
Adding user devops_1 to group admin
Done.
	amberlowe1001@DESKTOP-TV565H4:~$ su devops_1
		devops_1@DESKTOP-TV565H4:/home/amberlowe1001$ whoami
			devops_1