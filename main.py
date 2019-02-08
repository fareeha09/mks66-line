from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

display(screen)
save_extension(screen, 'img.png')

#for i in range(0, 500, 2):
 #       draw_line(i , i , 500, 500, screen, color)

p0x= 1
p0y= 1
p1x= 4
p1y= 1
p2x= 4
p2y= 5

#make triangles
for i in range(5):
    draw_line(p0x, p0y, p1x, p1y, screen, color)
    draw_line(p1x, p1y, p2x, p2y, screen, color) 
    draw_line(p2x, p2y, p0x, p0y, screen, color)
    p0x+=6
    p0y+=6
    p1x+=6
    p1y+=6
    p2x+=6
    p2y+=6

    


