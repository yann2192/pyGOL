#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from random import randint

class gameoflife:
    X = 50
    Y = 25
    def __init__(self):
        self.game = gameoflife.build()

    @staticmethod
    def build():
        res = []
        for x in range(gameoflife.X):
            res.append([])
            for y in range(gameoflife.Y):
                res[x].append(0)
        return res

    def get_neighbor(self, x, y):
        res = []
        if x > 0: res.append(self.game[x-1][y])
        if x < len(self.game)-1: res.append(self.game[x+1][y])
        if y > 0: res.append(self.game[x][y-1])
        if y < len(self.game[0])-1: res.append(self.game[x][y+1])
        if x > 0 and y > 0: res.append(self.game[x-1][y-1])
        if x < len(self.game)-1 and y < len(self.game[0])-1: res.append(self.game[x+1][y+1])
        if x < len(self.game)-1 and y > 0: res.append(self.game[x+1][y-1])
        if x > 0 and y < len(self.game[0])-1: res.append(self.game[x-1][y+1])
        return res

    def nb_neighbor_alive(self, x, y):
        return self.get_neighbor(x,y).count(1)

    def nb_neighbor_dead(self, x, y): 
        return self.get_neighbor(x,y).count(0)

    def process(self):
        tmp = gameoflife.build()
        for x in range(len(self.game)):
            for y in range(len(self.game[0])):
                if self.game[x][y] == 0:
                    if self.nb_neighbor_alive(x,y) == 3:
                        tmp[x][y] = 1
                    else: tmp[x][y] = 0
                else:
                    nb = self.nb_neighbor_alive(x,y)
                    if nb == 3 or nb == 2:
                        tmp[x][y] = 1
                    else: tmp[x][y] = 0
        self.game = tmp

    def init(self):
        for x in range(len(self.game)):
            for y in range(len(self.game[0])):
                self.game[x][y] = randint(0,1)

    def makemeaglider(self):
        x = 1
        y = 0
        self.game[x][y] = 1
        self.game[x+1][y+1] = 1
        self.game[x-1][y+2] = 1
        self.game[x][y+2] = 1
        self.game[x+1][y+2] = 1

    def __str__(self):
        os.system('clear')
        res = ""
        for y in range(len(self.game[0])):
            for x in range(len(self.game)):
                res += str(self.game[x][y])
            res += "\n"
        return res


if __name__ == '__main__':
    game = gameoflife()
    game.init()
    while True:
        print game
        raw_input()
        game.process()

