import socket
from argparse import ArgumentParser

def get_args():
    parser = ArgumentParser()
    parser.add_argument('domain', help='Domain to perform Office365 Check on')
    return parser.parse_args()

def banner():
    print "Office365 Check Tool"
    print "Author: Vincent Yiu (@vysecurity)"
    print "https://www.github.com/vysec/checkO365"
    print "Version: 1.0"
    print ""

def main():
    banner()
    args = get_args()
    domain = args.domain
    domain = domain.replace(".", "-")
    print "Checking: %s" % args.domain

    use = False

    url_dict = {
        "Global Office365": ".mail.protection.outlook.com",
        "NL Office365": ".mail.protection.outlook.de",
        "CN Office 365 (21vianet)": ".mail.protection.partner.outlook.cn",
        "other convention for Office365": ".mail.protection." + args.domain
    }

    for o365 in url_dict:
        try:
            host = socket.gethostbyname(domain + url_dict[o365])  # your os sends out a dns query
            print "[*] %s uses %s and resolves to: %s" % (args.domain, o365, host)
            print "> " + domain + url_dict[o365]
            use = True
        except:
            pass

    if not use:
        print "[!] %s does not seem to use Office365" % args.domain


if __name__ == '__main__':
    main()
