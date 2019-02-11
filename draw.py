from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    
	if x0>x1:
		#makes it so that we only work on the right side
		draw_line(x1,y1,x0,y0,screen,color)
		return
	
	dx= x1-x0
	dy= y1-y0
	
	#if slope is undefined
	if (dx == 0):
		for i in range(y1-y0):
			plot(screen, color, x0, y0+i)
	else:
                
        #if slope is 0
		if (dy == 0):
			for i in range(x1-x0):
				plot(screen, color, x0+i, y0)
				
		#octant 1-- also octant 5 kind of
		elif (dx >= dy > 0):
			octant1( x0, y0, x1, y1, dy, (-1 * dx), screen, color )
		#octant 2-- also octant 6 kind of
		elif (0 < dx < dy): 
			octant2( x0, y0, x1, y1, dy, (-1 * dx), screen, color )
		#octant 7 and 3 
		elif ((dy < 0) and (dx <= abs(dy))):
			octant7( x0, y0, x1, y1, dy, (-1 * dx), screen, color )
		#octant 8-- also octant 4 kind of
		elif((dy < 0) and (dx > abs(dy))):
			octant8( x0, y0, x1, y1, dy, (-1 * dx), screen, color )
    
def octant1( x0, y0, x1, y1, A, B, screen, color ):
	x=x0
	y=y0
	d = 2*A + B
	
	while (x <= x1):
		plot(screen, color, x, y)
		if d>0:
			y+=1
			d+=2*B
		x+=1
		d+=2*A
		
def octant2(x0, y0, x1, y1, A, B, screen, color ):
	x=x0
	y=y0
	d = A + 2*B
	
	while (y <= y1):
		plot(screen, color, x, y)
		if d<0:
			x+=1
			d+=2*A
		y+=1
		d+=2*B

def octant7( x0, y0, x1, y1, A, B, screen, color ):
	x=x0
	y=y0
	d = A - 2*B
	
	while (y >= y1):
		plot(screen, color, x, y)
		if d>0:
			x+=1
			d+=2*A
		y-=1
		d-=2*B

def octant8(x0, y0, x1, y1, A, B, screen, color ):
	x=x0
	y=y0
	d = 2*A - B
	
	while (x <= x1):
		plot(screen, color, x, y)
		if d<0:
			y-=1
			d-=2*B
		x+=1
		d+=2*A
