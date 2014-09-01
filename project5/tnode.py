###############################################
#
# Project 5		April 24, 2014
# Huffman Codes
#
# Matthew Leeds
# 
# File: tnode.py
#
###############################################

class TNode(object):
    """Represents a node for a linked binary search tree."""

    def __init__(self, letter = "", UID = 0, left = None, right = None):
        self.letter = letter
        self.left = left
        self.right = right
        self.UID = UID
        self.code = ""
    
    def __str__(self):
        return "Letter: " + str(self.letter) + " Left: " + str(self.left) + " Right: " + str(self.right) + "\n"

    def hasLeft(self):
        if self.left is not None: return True
        else: return False

    def hasRight(self):
        if self.right is not None: return True
        else: return False

    def setCode(self, code):
        self.code = code
