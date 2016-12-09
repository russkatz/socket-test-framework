#!/bin/bash

for host in `grep HOSTS defaults.cfg | awk -F= '{print$2}' | sed -e 's/,/ /g'`
do
	ssh $host /tmp/client.py &
done

sleep 1
echo ""
