#!/bin/bash

for host in `grep HOSTS defaults.cfg | awk -F= '{print$2}' | sed -e 's/,/ /g'`
do
	scp client.py $host:/tmp
	scp server.py $host:/tmp
	scp localstop.sh $host:/tmp
	scp defaults.cfg $host:/tmp
done

