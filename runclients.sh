#!/bin/bash

user=`grep SSH_USER defaults.cfg | awk -F= '{print$2}'`
for host in `grep HOSTS defaults.cfg | awk -F= '{print$2}' | sed -e 's/,/ /g'`
do
	ssh $user@$host /tmp/client.py &
done

sleep 1
echo ""
