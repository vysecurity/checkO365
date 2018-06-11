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
	domain = domain.replace(".","-")
	print "Checking: %s" % args.domain

	use = False
	
	try:
		host = socket.gethostbyname(domain + ".mail.protection.outlook.com") # your os sends out a dns query
		print "[*] %s uses Global Office365 and resolves to: %s" % (args.domain,host)
		print "> " + domain + ".mail.protection.outlook.com"
		use = True
	except:
		pass
		#print "[!] %s does not use Global Office365" % args.domain

	try:
		host = socket.gethostbyname(domain + ".mail.protection.outlook.de") # your os sends out a dns query
		print "[*] %s uses NL Office365 and resolves to: %s" % (args.domain,host)
		print "> " + domain + ".mail.protection.outlook.de"
		use = True
	except:
		pass
		#print "[!] %s does not use NL Office365" % args.domain

	try:
		host = socket.gethostbyname(domain + ".mail.protection.partner.outlook.cn") # your os sends out a dns query
		print "[*] %s uses CN Office365 (21vianet) and resolves to: %s" % (args.domain,host)
		print "> " + domain + ".mail.protection.partner.outlook.cn"
		use = True
	except:
		pass
		#print "[!] %s does not use CN Office365" % args.domain

	try:
		host = socket.gethostbyname(domain + ".mail.protection." + args.domain) # your os sends out a dns query
		print "[*] %s uses other convention for Office365 and resolves to: %s" % (args.domain,host)
		print "> " + domain + ".mail.protection." + args.domain
		use = True
	except:
		pass
		#print "[!] %s does not use other Office365" % args.domain

	if not use:
		print "[!] %s does not seem to use Office365" % args.domain


if __name__ == '__main__':
    main()