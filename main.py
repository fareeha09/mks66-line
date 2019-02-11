from display import *
from draw import *

screen = new_screen()
color = [ 139, 69, 19 ]

display(screen)
save_extension(screen, 'img.png')

#make triangles
#for i in range(5):
draw_line( 0, 0, 300, 300, screen, color )
    


