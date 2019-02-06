from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

display(screen)
save_extension(screen, 'img.png')

#start (0,0); end (10,9)
draw_line(0 , 0 , 10, 9, screen, color)
