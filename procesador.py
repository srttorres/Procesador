import sys

def main():
	inputfile = ''
	if (len(sys.argv) == 1):
		print "Usage: procesador.py <inputfile>"
		sys.exit(2)
	inputfile = sys.argv[1]
	print "OK"
	sys.exit(0)

if __name__ == '__main__':
	main()