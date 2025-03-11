# Isabel Ojeda
# HW5 Q2
from collections import deque

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
	
	def __str__(self):
		return self.value

def traverse(root):

   
        

e = Node("E")
d = Node("D")
c = Node("C", d, e)
b = Node("B")
root = Node("A", b, c)

for v in traverse(root):
    print(v)  # Expected Output: A B C D E
