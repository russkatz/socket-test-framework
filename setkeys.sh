#!/bin/bash

for host in `grep HOSTS defaults.cfg | awk -F= '{print$2}' | sed -e 's/,/ /g'`
do
	ssh-copy-id $host
done

