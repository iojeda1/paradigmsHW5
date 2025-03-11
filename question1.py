# Isabel Ojeda
# HW5 Q1

def move_robot(n): 
    # north, east, suth, west
    dir = [(0,1), (1,0), (0,-1), (-1, 0)] 
    res = [(0,0)] 
    i = 0 
    m = 1
    x = 0
    y = 0
    for r in range(n):
        dirx, diry = dir[i]
        x += m*dirx
        y += m*diry
        res.append((x,y))
        i = (i+1)%4 # clockwise direction
        m += 1
    return res 

for v in move_robot(4):
    print(v)
for v in move_robot(0):
	print(v)
for v in move_robot(2):
	print(v)