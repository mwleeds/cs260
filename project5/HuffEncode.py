################################################
#
#  Project 5    April 15, 2014
#  Huffman Codes
#
#  Matthew Leeds
#
#  File: HuffEncode.py
#
################################################

from bstnode import BSTNode
from counter import Counter
from arrayheap import ArrayHeap

def main():
	# add each line in counts to a priority queue that will sort it
	# storing them as BST Nodes with data and letter members
	counts = open('counts.txt','r')
	print(">> Building a Huffman code tree from file counts.txt...", end='')
	HuffQueue = ArrayHeap()
	for line in counts:
		temp = BSTNode(int(line[line.index(' '):len(line)-1]),line[:line.index(' ')])
		HuffQueue.add(temp)

	# form a tree using the queue that has the lowest 
	# frequency items at the lowest levels
	UIDgen = Counter()
	while len(HuffQueue) >= 2:
		leftSubtree = HuffQueue.pop()
		rightSubtree = HuffQueue.pop()
		newFreq = leftSubtree.data + rightSubtree.data
		UID = UIDgen.getNext()
		HuffQueue.add(BSTNode(newFreq, "", UID, leftSubtree, rightSubtree))
	rootNode = HuffQueue.pop()
	print("Done.\n")

	# traverse the tree (preorder and inorder) and output these to files
	# Internal nodes will be printed as I:xxx with xxx being a unique id
	# Leaf nodes will be L:xxx where xxx is the ASCII value
	preordertxt = open('preorder.txt','w')
	def preorder(probe):
		if probe is not None:
			if probe.hasLeft() or probe.hasRight():
				preordertxt.write("I:" + str(probe.UID) + "\n")
				preorder(probe.left)
				preorder(probe.right)
			else:
				preordertxt.write("L:" + probe.letter + "\n")
	
	preorder(rootNode)	

	inordertxt = open('inorder.txt','w')
	def inorder(probe):
		if probe is not None:
			if probe.hasLeft(): 
				inorder(probe.left)
			if probe.hasLeft() or probe.hasRight():
				inordertxt.write("I:" + str(probe.UID) + "\n")
			else:
				inordertxt.write("L:" + probe.letter + "\n")
			if probe.hasRight():
				inorder(probe.right)
			
	inorder(rootNode)

	# Use the tree to generate Huffman codes for each character and output them to codetable.txt
	codetable = open('codetable.txt','w')
	print(">> Writing file codetable.txt based on the Huffman tree...", end='')
	def buildcode(probe, huffCode=""):
		if not probe.hasLeft() and not probe.hasRight():
			codetable.write(probe.letter + " " + probe.code + "\n")
		else:
			if probe.hasLeft():	
				probe.left.setCode(huffCode + "0")
				buildcode(probe.left, probe.left.code)
			if probe.hasRight(): 
				probe.right.setCode(huffCode + "1")
				buildcode(probe.right, probe.right.code)
		
	buildcode(rootNode)
	print("Done.\n")
	counts.close()
	preordertxt.close()
	inordertxt.close()
	codetable.close()
	
if __name__=="__main__": 
	main()
