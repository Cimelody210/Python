import pygame
import turtle as rua
import random

from setting import *
from ursina import *
from math import *
from freegames import square, vector

screen = pygame.display.set_mode((WIDTH =800,HEIGHT = 400), pygame.RESIZABLE)
name = str(name)
vukhi = []

def Heart(k):
    return 15*sin(k)**3

class NhanVat:
    def __init__(self, name, gioitinh, HP, vukhi):
        self.name = name
        self.gioitinh = gioitinh
        self.HP =HP
        self.vukhi = vukhi

def Attack():
    pass
def Die():
    pass
def Move():
    pass

pygame.init()
