#!/usr/bin/python3.6
import dns.resolver
import argparse
import tldextract
import re
defaultpath = '/var/log/dnsresult.log'
open(defaultpath, "w").close()
ap = argparse.ArgumentParser(prog="DNSChecker")
ap.add_argument("--output", "-o", help="Location to which results are saved, /var/log/dnsresult.log if no location given ", default="/var/log/dnsresult.log")
ap.add_argument("--version", "-v", action="version", version="%(prog)s 1.07", help="Version of DNSChecker")
ap.add_argument("--mailserver", "-m", help="To get only the Mail server informations of your domain")
ap.add_argument("--arecord", "-a", help="To get the A record of your domain only")
ap.add_argument("--txt", "-t", help="To get TXT and SPF of the domain only")
ap.add_argument("--nameservers", "-ns", help="List the name servers of the domain")
ap.add_argument("--allrecords", "-all", help="Get the DNS records of the domain - A, MX, PTR(RDNS), TXT & SPF")
args = ap.parse_args()
path = args.output
arec = args.arecord
txtrec = args.txt
mx = args.mailserver
allrecords = args.allrecords
ns = args.nameservers

# URL stripper
def stripper(stripe_url):
 stripped = re.sub(r'https://www\.|http://www\.|https://www|http://|https://|www\.', "", stripe_url).strip('/')
 return stripped

# 'A' record and RDNS
def anptrrecord():
    try:
        arec_d = stripper(arec)
        answera = dns.resolver.query(arec_d, 'A')
        lengtha = len(answera)
        hashunder_a = '#'*31
        fo = open(path,"a")
        fo.write("\nA record and RDNS of the domain\n"+str(hashunder_a)+"\n\n"+arec_d+ " is resolving from "+str(lengtha)+ " servers\n"+"\nA records are :\n\n")
        fo.close()
        for rdata in answera:
            dnsarecord = rdata.address
            try:
                qname = dns.reversename.from_address(dnsarecord)
                answerptr = dns.resolver.query(qname, 'PTR')
                for ptr in answerptr:
                    fo = open(path,"a")
                    fo.write(dnsarecord+"\n\nRDNS/PTR record of the IP address "+dnsarecord+" is "+str(ptr)+"\n\n")
                    fo.close()
            except:
                fo = open(path,"a")
                fo.write("\n"+dnsarecord+"\n\nThe IP address "+dnsarecord+" don't have RDNS/PTR\n")
                fo.close()
        return
    except:
        fo = open(path,"a")
        fo.write("\nERROR !!!\n\nPlease enter a valid website URL. (i.e. www.example.com or example.com or http://example.com/ or https://example.com/\n"+" ***If you are certain that you have provided an active domain, make sure that it contains a domain name only !\n" )
        exit()

#MX Mail server check
def mxrecord():
    hashunder = '#'*19
    try:
        mxd = stripper(mx)
        answersmx = dns.resolver.query(mxd, 'MX')
        lengthmx = len(answersmx)
        fo = open(path,"a")
        fo.write("\n\nMail server details\n"+str(hashunder)+"\n\nNumber of mail servers are :  "+str(lengthmx)+"\n")
        fo.close()
        for rdata in answersmx:
            fo = open(path,"a")
            fo.write("\nMail server "+str(rdata.exchange)+" has a preference of "+str(rdata.preference)+"\n")
            fo.close()
            print('\n')
        return
    except:
        fo = open(path,"a")
        fo.write("\n\nMail server details\n"+str(hashunder)+"\n\nPlease enter a valid website URL. (i.e. www.example.com).\n"+" ***If you are certain that the provided domain is a valid one, then the domain don't have a mail server defined !\n\n")
        fo.close()

#TXT and SPF records
def txtnspf():
    try:
        txtrec_d = stripper(txtrec)
        answerstxt = dns.resolver.query(txtrec_d, 'TXT')
        length = len(answerstxt)
        hashundertxt = '#'*41
        fo = open(path,"a")
        fo.write("\n\n\nTXT (SPF and domain verification records)\n"+str(hashundertxt)+"\n\nNumber of TXT records :  "+str(length)+"\n")
        fo.close()
        for rdata in answerstxt:
            for txt_string in rdata.strings:
                fo = open(path,"a")
                fo.write("\nTXT : "+str(txt_string)+"\n\n")
                fo.close()
        print("\n")
        return
    except:
        hashundertxt = '#'*41
        fo = open(path,"a")
        fo.write("\n\n\nTXT (SPF and domain verification records)\n"+str(hashundertxt)+"\n\nPlease enter a valid website URL. (i.e. www.example.com or example.com or http://example.com/ or https://example.com/.\n"+" \n***If you are certain that you have provided a valid domain, the domain don't have TXT/SPF records !\n\n")
        fo.close()

#Name servers

def nameserver():
    try:
        ext = tldextract.extract(ns)
        nsrs = ext.registered_domain
        nameservers = dns.resolver.query(nsrs,'NS')
        length = len(nameservers)
        hashunderns = '#'*18
        fo = open(path,"a")
        fo.write("\nName servers are :\n"+str(hashunderns)+"\n\n")
        fo.close()
        for data in nameservers:
            fo = open(path,"a")
            fo.write(str(data)+"\n")
            fo.close()
            print("\n")
        return
    except:
        print("\nPlease make sure that you have provided an active/registerd domain !\n")

#Ask for help
def askhelp():
    print("\nUse --help or -h to find the arguments suitable for your requriement !\n")

#Comparison of commandline arguments
if args.mailserver:
   mxrecord()
elif args.arecord:
   anptrrecord()
elif args.txt:
   txtnspf()
elif args.nameservers:
   nameserver()
elif args.allrecords:
   mx = arec = txtrec = ns = args.allrecords
   anptrrecord()
   mxrecord()
   txtnspf()
   nameserver()
else:
   askhelp()