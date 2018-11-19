# GetDNSrecords



     DNSChecker 1.07
     ###############

Script to get the DNS A, RDNS, MX, NS and TXT records in a text or any file format you are providing.


USAGE :


         #./dns_checker.py --help

usage: DNSChecker [-h] [--output OUTPUT] [--version] [--mailserver MAILSERVER]
                  [--arecord ARECORD] [--txt TXT] [--nameservers NAMESERVERS]
                  [--allrecords ALLRECORDS]

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Location to which results are saved,
                        /var/log/dnsresult.log if no location given
  --version, -v         Version of DNSChecker
  --mailserver MAILSERVER, -m MAILSERVER
                        To get only the Mail server informations of your
                        domain
  --arecord ARECORD, -a ARECORD
                        To get the A record of your domain only
  --txt TXT, -t TXT     To get TXT and SPF of the domain only
  --nameservers NAMESERVERS, -ns NAMESERVERS
                        List the name servers of the domain
  --allrecords ALLRECORDS, -all ALLRECORDS
                        Get the DNS records of the domain - A, MX, PTR(RDNS),
                        TXT & SPF



The default location of the output/results will be at ‘/var/log/dnsresult.log’, you can choose the output location as the command line argument. The output log will be cleared each time when the script executed. Also the script will provide the results for valid/active domains only.


REQUIREMENTS:

This script will run on Python 3.x versions only.

Below are the additional modules you need to install to work this script.

    dnspython
    argparse
    tldextract
    re

Once you have installed Python 3.x version, you can install the modules using 'pip' - package management system used to install and manage software packages written in Python.


For example, if you are installed Python 3.6.5 version, then use the below commands to install the required modules for this script.


    #pip3.6 install dnspython
   
    #pip3.6 install argparse
   
    #pip3.6 install tldextract



