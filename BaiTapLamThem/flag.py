from turtle import *
from math import sin, cos, pi
from time import perf_counter

bgcolor("#f00")
setup(600,400,800,30)
hideturtle()
tracer(0)
penup()

def MTGPMNVN():
    update()
    clear()
    t =  perf_counter()*3
    goto(0,-9999)
    dot(9999*2, (0,0.5,1))
    color("#ff0")
    begin_fill()
    for i in range(401):
        a =(i/400)*4*pi
        R = 50 / cos(a%(pi*4/5)- pi*4/5/2)
        goto( R* cos(a*pi/2)+ 2*cos(t-R),R* sin(a*pi/2)+ 2*sin(t-R))
    end_fill()
    ontimer(MTGPMNVN, 10)

MTGPMNVN()
# Run in python version 3.11 and lower
