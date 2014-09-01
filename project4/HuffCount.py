################################################
#
#  Project 4    April 13, 2014
#  Huffman Codes
#
#  Matthew Leeds
#
#  File: HuffCount.py
#
################################################

def main():
	counts = {}
	# Read in each character from the source and 
	# keep a count of the instances of each in a dictionary, counts
	with open('source.txt','r') as source:
		for line in source:
			for char in line:
				if char not in counts:
					counts[char] = 1
				else:
					counts[char] += 1

	# output the counts to a counts.txt file as "ASCIIVALUE NUMBEROFINSTANCES"
	# in order of increasing ASCII value
	countsFile = open('counts.txt','w')
	for i in range(129):
		if chr(i) in counts:
			countsFile.write(str(i) + " " + str(counts[chr(i)]) + "\n")
	
	source.close()
	countsFile.close()

if __name__=="__main__":
	main()
