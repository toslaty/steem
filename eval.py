import requests
import argparse


def openfi(list,domain,fi):
	f = open(list,"r")
	for line in f:
		try:
			line = line.rstrip('\r\n')
			req(line, domain,fi)	
		except:
			continue	

def req(word,domain,fi):
	d = 'https://'+word+'.'+domain
	x = requests.get(d)
	if x.status_code == 200:
		writeto(word, d, fi)

def writeto(sub, d, name):
	print d
	o = open(name, "w")
	o.write(d)
	o.close()


def main():

	parser = argparse.ArgumentParser(prog="eval", usage="%(prog)s [options]")
	parser.add_argument("-i","--inp", help="input wordlist")
	parser.add_argument("-w","--wri", help="output list with subdomains")
	parser.add_argument("-d", "--domain", help="the domain e.g. google.com")

	args = parser.parse_args()

	if not args.inp or not args.wri or not args.domain:
		parser.print_help()

	openfi(args.inp,args.domain, args.wri)


if __name__ == "__main__":
	main()
