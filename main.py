from display import *
from draw import *

screen = new_screen()
color = [ 139, 69, 19 ]

#creates grid
for i in range(0, 500, 5):
	if (i == 250):
		draw_line(i-1, 0, i-1, 500, screen, color)
		draw_line(i+1, 0, i+1, 500, screen, color)
		draw_line(0, i-1, 500, i-1, screen, color)
		draw_line(0, i+1, 500, i+1, screen, color)
	draw_line(i, 0, i, 500, screen, color)
	draw_line(0, i, 500, i, screen, color)

color1 = [ 0, 0, 0 ]
draw_line(0,0,400,500, screen, color1)
draw_line(0,1,400,501, screen, color1)

#creates y
draw_line(390,450, 400, 430, screen, color1)
draw_line(391,450, 401, 430, screen, color1)
draw_line(400, 430, 410, 450, screen, color1)
draw_line(401, 430, 411, 450, screen, color1)
draw_line(400, 430, 390, 410, screen, color1)
draw_line(401, 430, 391, 410, screen, color1)

#creates =
draw_line(420,441, 440, 441, screen, color1)
draw_line(420,440, 440, 440, screen, color1)
draw_line(420,434, 440, 434, screen, color1)
draw_line(420,435, 440, 435, screen, color1)

#creates question mark
draw_line(450,450, 455, 455, screen, color1)
draw_line(450,449, 455, 454, screen, color1)

draw_line(455,455, 460, 458, screen, color1)
draw_line(455,454, 460, 457, screen, color1)

draw_line(460,458, 465, 458, screen, color1)
draw_line(460,457, 465, 457, screen, color1)

draw_line(465,458, 470, 455, screen, color1)
draw_line(465,457, 470, 454, screen, color1)

draw_line(470,455, 475, 450, screen, color1)
draw_line(470,454, 475, 449, screen, color1)

draw_line(475,450, 477, 445, screen, color1)
draw_line(474,449, 476, 444, screen, color1)

draw_line(477, 445, 475, 440, screen, color1)
draw_line(476, 444, 475, 439, screen, color1)

draw_line(475, 440, 465, 435, screen, color1)
draw_line(474, 439, 464, 434, screen, color1)

draw_line(465, 435, 464, 425, screen, color1)
draw_line(464, 434, 463, 424, screen, color1)

draw_line(464, 420, 462, 418, screen, color1)
draw_line(464, 419, 462, 417, screen, color1)

draw_line(462, 418, 464, 416, screen, color1)
draw_line(462, 417, 464, 415, screen, color1)

draw_line(464, 416, 466, 418, screen, color1)
draw_line(464, 415, 466, 417, screen, color1)

draw_line(466, 418, 464, 420, screen, color1)
draw_line(466, 417, 464, 419, screen, color1)


display(screen)
save_extension(screen, 'img.png')

#make triangles
#for i in range(5):


