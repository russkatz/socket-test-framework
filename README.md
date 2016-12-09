# socket-test-framework
These simple scripts will test the connectivity between multiple hosts across muliple ports by trying to open a socket between every host and port combination. I created these scripts when I needed to verify firewalls were configured correctly before installing DSE on a locked down network with no external connectivity, no tools like nc, no compilers, and no root access. The only requirements are python, bash, and ssh. Hosts and ports are configurable so this is not limited to pre-flight checking for DSE.

# Quick Start
* Clone repository to machine with SSH access to all the hosts you want to test. Can be ran from one of the hosts being tested.
* Edit defaults.cfg and set the hosts and ports you want to test, and ssh user to connect to the servers being tested with.
* [Optional] Create ssh key on local machine: ssh-keygen -t rsa
* [Optional] Run ./setkeys.sh to push SSH key to all machines being tested. You will be prompted to enter the SSH user's password once per host
* Push framework to the hosts: ./push.sh [If you update defaults.cfg re-run this]
* Start server to each host to listen on the ports: ./startservers.sh
* Run tests on every host: ./runclients.sh
* Stop the server on all hosts: ./stopservers.sh
