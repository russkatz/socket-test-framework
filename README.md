# socket-test-framework
A sample framework to test the connectivity between multiple hosts across muliple ports by trying to open a socket between every host and port combination. The framework consists of a server to listen on the ports, a client to verify it can reach the server ports, and scripts to manage installing/starting/stopping the framework.

I created these scripts when I needed to verify firewalls were configured correctly before installing Datastax Enterprise on a locked down network with no external connectivity, no tools like nc, no compilers, and no root access. The only requirements are python, bash, and ssh. Hosts and ports are configurable so this is not limited to pre-flight checking for DSE.

# Quick Start
* Clone/copy repository to machine with SSH access to all the hosts you want to test. Can be ran from one of the hosts being tested.
* Edit defaults.cfg and set the hosts and ports you want to test, and ssh user to connect to the servers being tested with.
* [Optional] Create ssh key on local machine: ssh-keygen -t rsa
* [Optional] Run ./setkeys.sh to push SSH key to all machines being tested. You will be prompted to enter the SSH user's password once per host
* Push framework to the hosts: ./push.sh [If you update defaults.cfg re-run this]
* Start server on each host to listen on the ports to be tested: ./startservers.sh
* Run tests on every host: ./runclients.sh
* Stop the server on all hosts: ./stopservers.sh

# Limitations
* Currently installs the framework on the hosts in /tmp, should make this configurable
* The SSH username has to be the same on all hosts
