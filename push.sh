#!/bin/bash

user=`grep SSH_USER defaults.cfg | awk -F= '{print$2}'`
for host in `grep HOSTS defaults.cfg | awk -F= '{print$2}' | sed -e 's/,/ /g'`
do
	scp client.py $user@$host:/tmp
	scp server.py $user@$host:/tmp
	scp localstop.sh $user@$host:/tmp
	scp defaults.cfg $user@$host:/tmp
done

