################################################
#
#  Project 5    April 24, 2014
#  Huffman Codes
#
#  Matthew Leeds
#
#  File: HuffDecode.py
#
################################################

from tnode import TNode
from arrayheap import ArrayHeap

def main():
	print(">> Building the Huffman code tree based on file preorder.txt...", end='')
	# import just the preorder traversal because the nodes are labeled as iternal or leaf
	preorder = open('preorder.txt','r')
	preList = []
	for line in preorder:
		preList.append(line[:len(line)-1])
	index = 0 # used to track where we are in preList

	def buildtree():
		# this function takes the index of an internal node (in preList)
		# stored in index and returns a tree built from it
		nonlocal index
		tempNode = TNode('')
		index += 1
		if (preList[index])[0] == 'I':
			tempNode.left = buildtree()
			index += 1
			if (preList[index])[0] == 'I':
				tempNode.right = buildtree()
			else:
				letter = (preList[index])[2:len(preList[index])]
				tempNode.right = TNode(letter)	
		else: # for leaf nodes, just add them to left and right of tempNode
			letter = (preList[index])[2:len(preList[index])]
			tempNode.left = TNode(letter)
			# Now check on the right side and build that tree
			index += 1
			if (preList[index])[0] == 'I':
				tempNode.right = buildtree() 
			else:
				letter = (preList[index])[2:len(preList[index])]
				tempNode.right = TNode(letter)
		return tempNode
	rootNode = buildtree()
	print("Done.\n")

	# Now traverse through the source file and use the tree 
	# to find the appropriate encoding for each character.
	encoded = open('HuffmanOutput.txt','r')
	decoded = open('sourceDecoded.txt','w')
	probe = rootNode
	print(">> Decoding HuffmanOutput.txt into sourceDecoded.txt using the tree...", end='')
	def checkleaf():
		# checks if we're at the leaf node, and if so writes the 
		# appropriate character to the output file and resets the probe to the root node
		nonlocal probe
		if not(probe.hasLeft() or probe.hasRight()): # leaf
			decoded.write(chr(int(probe.letter)))
			probe = rootNode

	for line in encoded:
		for bit in line:
			# for each character, go left or right in the tree 
			# and check if we're at a leaf node
			if bit == '0':
				probe = probe.left
				checkleaf()
			elif bit == '1':
				probe = probe.right 
				checkleaf()
	print("Done.\n")

	encoded.close()
	decoded.close()
	preorder.close()

if __name__=="__main__":
	main()	
