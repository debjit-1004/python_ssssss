import turtle

n=int(input('enter the value of n for n-gon'))
t=turtle.Turtle()
for i in range(1,n+1):
    degree=360/n
    t.forward(40)
    t.left(degree)

turtle.exitonclick()
