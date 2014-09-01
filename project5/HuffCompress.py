################################################
#
#  Project 5    April 24, 2014
#  Huffman Codes
#
#  Matthew Leeds
#
#  File: HuffCompress.py
#
################################################

def main():
	print(">> Compressing source.txt into HuffmanOutput.txt...", end='')
	codedict = {}
	codetable = open('codetable.txt','r')
	# read in the codetable created with HuffCount.py and HuffEncode.py
	# into a dictionary as codedict[ASCIIvalue] = "bit encoding"
	for line in codetable:
		charindex = line.index(' ')
		codedict[line[:charindex]] = line[charindex+1:len(line)-1]
	# read in the source.txt file and use the dictionary to "compress" it,
	# outputting to HuffmanOutput.py
	source = open('source.txt','r')
	output = open('HuffmanOutput.txt','w')
	for line in source:
		for char in line:
			encoding = codedict.get(str(ord(char)), "") # default value of an empty string
			output.write(encoding)
	print("Done.\n")
	codetable.close()
	source.close()
	output.close()

if __name__=="__main__":
	main()	
