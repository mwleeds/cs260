###############################################
#
# Project 5 	April 24, 2014
# Huffman Codes
#
# Matthew Leeds
# 
# File: bstnode.py
#
###############################################

class BSTNode(object):
    """Represents a node for a linked binary search tree."""

    def __init__(self, data, letter, UID = 0, left = None, right = None):
        self.data = data
        self.letter = letter
        self.left = left
        self.right = right
        self.UID = UID
        self.code = ""
    
    def __str__(self):
        return "Data: " + str(self.data) + " letter: " + str(self.letter)

    def hasLeft(self):
        if self.left is not None: return True
        else: return False

    def hasRight(self):
        if self.right is not None: return True
        else: return False

    def setCode(self, code):
        self.code = code
