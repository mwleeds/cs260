################################################
#
#  Project 5    April 13, 2014
#  Huffman Codes
#
#  Matthew Leeds
#
#  File: counter.py
#
################################################

class Counter(object):

	def __init__(self, val=999):
		self.val = val

	def getNext(self):
		self.val += 1
		return self.val

	def reset(self):
		self.val = 999
