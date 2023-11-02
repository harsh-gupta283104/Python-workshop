import turtle
import msvcrt

pen=turtle.Turtle()
 
def move(arrow):
    if arrow==b'1':
        pen.forward(1)
    if arrow==b'2':
        pen.backward(1)
    if arrow==b'3':
        pen.right(90)
    if arrow==b'4':
        pen.left(90)
    if arrow==b'5':
        pen.left(1)
        pen.forward(1)
    if arrow==b'6':
        pen.right(1)
        pen.forward(1)
        
                                
 
   
while True:
    arrow = msvcrt.getch().lower()
    move(arrow)
    turtle.update()
