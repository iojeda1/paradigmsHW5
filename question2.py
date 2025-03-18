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
	res = []
	q = deque([root])
	level = 1
	while q:
		size = len(q)
		nodes = []
		for _ in range(size):
			node = q.popleft()
			nodes.append(node)
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)
		if level % 2 == 1: # if the level is odd go from right to left 
			nodes.reverse() # reverse nodes in place
		for n in nodes:
			res.append(n)
		level += 1
	return res

e = Node("E")
d = Node("D")
c = Node("C", d, e)
b = Node("B")
root = Node("A", b, c)
for v in traverse(root):
    print(v)  # Expected Output: A B C E D

print('\n')
gg = Node("G", None, None)
f = Node("F", None, None)
e = Node("E", None, None)
d = Node("D", None, None)
c = Node("C", f, gg)
b = Node("B", d, e)
root = Node("A", b, c)
for v in traverse(root):
	print(v)

print('\n')
node9 = Node("Node9", None, None)
node10 = Node("Node10", None, None)
node7 = Node("Node7", None, None)
node8 = Node("Node8", node9, node10)
node5 = Node("Node5", None, None) 
node6 = Node("Node6", node7, node8)
node3 = Node("Node3", None, None)  
node4 = Node("Node4", node5, node6)
node1 = Node("Node1", node3, node4)
node2 = Node("Node2", None, None)  
root = Node("Root", node1, node2)
for v in traverse(root):
	print(v)