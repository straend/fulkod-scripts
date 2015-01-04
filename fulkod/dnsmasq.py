
class DNSMasq():
    servers =[]
    domains = []

    def __init__(self, servers):
        self.servers = servers

    def addDomain(self,domain):
        self.domains.append(domain)

    def getConf(self):
        for domain in self.domains:
            for server in self.servers:
                yield "server=/%s/%s"%(domain, server)


if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='get simple DNSmasq conf for Unotelly like services')

    parser.add_argument('--file', type=str, nargs=1,default=None,help="Read from file instead of STDIN")
    parser.add_argument('--save', type=str, nargs=1,default=None,help="Write to file instead of STDOUT")

    parser.add_argument('servers', metavar='server', type=str, nargs='+', help='dns servers')

    args = parser.parse_args()
    d = DNSMasq(args.servers)
    filenames = args.file

    if filenames is None:
        for line in sys.stdin:
            d.addDomain(line.strip())
    else:
        for filename in filenames:
            with open(filename) as file:
                for line in file:
                    d.addDomain(line.strip())
        file.close()

    if args.save is None:
        for line in d.getConf():
            print(line)
    else:
        with open(args.save[0], 'w') as file:
            for line in d.getConf():
                file.write("%s\n" %line)
        file.close()
