#!/usr/bin/python2
class Player(object):
    avail = ('avail',(0,0))

    def __init__(self,color,bonusfigures=[]):
        self.figures = [self.avail]*7
        self.bonusfigures=bonus
        self.points = 0
        self.color = color

