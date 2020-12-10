import turtle
color=["red","green","Yellow","teal"]
window=turtle.Screen()
alex=turtle.Turtle()
nav=turtle.Turtle()


#alex.fillcolor("white")
#alex.begin_fill()

#
#for _ in range(10):
 #   alex.forward(0)
  #  alex.shape("turtle")
    

#alex.end_fill()


#nav.fillcolor("red")
#nav.begin_fill()
nav.penup()
for _ in range(8):
    nav.stamp()
    nav.forward(50)
    nav.left(45)

#nav.end_fill()





window.mainloop()
