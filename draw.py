from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    #if slope is undefined
    if ((x1-x0) == 0):
        for i in range(y1-y0):
            plot(screen, color, x0, y0+i)
    else:
        slope = (y1 - y0)/(x1 - x0)
        
        #if slope is 0
        if (slope == 0):
            for i in range(x1-x0):
                plot(screen, color, x0+i, y0)
    
