#!/usr/bin/env bash

proxy_host="example.proxy.local"
proxy_port="8080"
uri="http://www.google.com/"

# This is the STDIN for telnet, keep in mind that this needs to be running
# as long as the request is handled. You can test the result by removing the
# sleep.
send_headers () {
  # Note the use of HTTP/1.0. 1.1 would keep the connection open
  # and you will need to wait for the 10 second timout below.
  echo "GET $uri HTTP/1.0"
  echo
  echo
  # 10 second timeout to keep STDIN open
  sleep 10
}

# This reads the telnet output per line, do your stuff here
while read -r line; do
  echo "$line"
done < <(telnet "$proxy_host" "$proxy_port" < <(send_headers))