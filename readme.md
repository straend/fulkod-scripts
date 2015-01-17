#Ehlo

This is the place where You will find small scripts, that I use for something.
It might be useful for You, but probably not


/Tomas <tomas+gh@fik1.net>

##dnsmasq.py

generates config for dnsmasq to use supplied dns server for domains specifed in textfile wih --file or piped.
Usage:
    
    dnsmasq.py --file domainslist.txt --save output.txt "ip address to dns server" "second dns server"
    
if --save is omitted output will be written to STDOUT
    
if --file is omitted the script will read domains from STDIN, one domain per line

