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
