from Tkinter import *
import tkMessageBox
import random
import threading
import time

import sys


"""
 --------> x
 |
 |
 |
\|/
 y
"""


class Background(object):
    def __init__(self):
        self.root = Tk()

    def draw(self, game_height=15, game_width=15):
        self.cv = Canvas(self.root, bg='white', height=20 * game_height, width=20 * game_width)
        self.cv.pack()


class Snake(object):
    def __init__(self, background, grid_size=20, game_height=15, game_width=15):
        # initial position(20,20),grid_size:20, direction: 0 and 1 are horizontal, 2 and 3 are vertical
        self.x = grid_size
        self.y = grid_size
        self.grid_size = grid_size
        self.direction = 3
        self.body_length = 4

        self.background = background

        self.game_height = game_height
        self.game_width = game_width

        # { {x0,y0}, {x1,y1}, ...,{xn,tn} }
        self.snake_coord = []
        self.block = []
        for i in range(self.body_length):
            coord = [self.x + self.grid_size, self.y]
            self.x = self.x + self.grid_size
            self.snake_coord.append(coord)
            rt = self.background.cv.create_rectangle(self.x, self.y, self.x + self.grid_size, self.y + self.grid_size, fill='blue')
            self.block.append(rt)
            self.background.cv.pack()

    def eat(self):
        coord = self.snake_coord[self.body_length - 1]
        self.snake_coord.append(coord)
        rt = self.background.cv.create_rectangle(coord[0], coord[1], coord[0] + self.grid_size, coord[1] + self.grid_size, fill='blue')
        self.block.append(rt)
        self.background.cv.pack()
        self.body_length = self.body_length + 1

    def move(self):
        # draw other blocks
        for i in range(1, self.body_length):
            self.snake_coord[self.body_length - i] = self.snake_coord[self.body_length - i - 1]
            x = self.snake_coord[self.body_length - i][0]
            y = self.snake_coord[self.body_length - i][1]
            self.background.cv.coords(self.block[self.body_length - i], (x, y, x + self.grid_size, y + self.grid_size))
        x = self.snake_coord[0][0]
        y = self.snake_coord[0][1]
        if self.direction == 0:
            x = x + self.grid_size
        elif self.direction == 1:
            x = x - self.grid_size
        elif self.direction == 2:
            y = y - self.grid_size
        elif self.direction == 3:
            y = y + self.grid_size
        temp = [x, y]
        self.snake_coord[0] = temp
        # draw the first block
        self.background.cv.coords(self.block[0], (x, y, x + self.grid_size, y + self.grid_size))
        self.checkConflict()

    def checkConflict(self):
        # check wall, only with the head
        x = self.snake_coord[0][0]
        y = self.snake_coord[0][1]
        if x < 0 or x == self.grid_size * self.game_width or y < 0 or y == self.grid_size * self.game_height:
            print "hit the wall"
            tkMessageBox.showerror("Game Over", "You hit the wall")

        # check the body
        for i in range(1, self.body_length):
            if x == self.snake_coord[i][0] and y == self.snake_coord[i][1]:
                print "hit the body", i, x, " ", self.snake_coord[i][0], " ", y, self.snake_coord[i][1]
                tkMessageBox.showerror("Game Over", "You hit the body")


class Food(object):
    def __init__(self, background, game_width=15, game_height=15, grid_size=20):
        self.height_boundry = game_height
        self.width_boundry = game_width
        self.grid_size = grid_size
        self.background = background
        self.rt = None

    def generate(self, snake_body, init_mode=False):
        # random
        inBody = 1
        number = len(snake_body)
        while(inBody == 1):
            inBody = 0
            x = self.grid_size * random.randint(1, self.width_boundry - 1)
            y = self.grid_size * random.randint(1, self.height_boundry - 1)
            #check if food colide with snake
            for i in range(number):
                if x == snake_body[i][0] and y == snake_body[i][1]:
                    inBody = 1
                    break
        self.coord = [x, y]     
        if init_mode:
            self.rt = self.background.cv.create_rectangle(x, y, x + self.grid_size, y + self.grid_size, fill='green')
        self.background.cv.coords(self.rt, (x, y, x + self.grid_size, y + self.grid_size))


class SnakeGame(object):
    def __init__(self, background, game_height=15, game_width=15, period=0.3):
        self.background = background
        self.game_height = game_height
        self.game_width = game_width
        self.period = period

        self.snake = Snake(background)
        self.food = Food(background)
        self.food.generate(self.snake.snake_coord, init_mode=True)
        self.entry = Entry(self.background.root)
        self.has_new_food = True
    
    def init_game(self):
        t1 = threading.Thread(target=self.move)
        t1.start()

        t2 = threading.Thread(target=self.listenKeyboard)
        t2.start()

    def changedirection(self, event):
        # print('You have entered: ', event.char)
        # use "w,a,s,d" to control direction
        if event.char == 'w':
            if self.snake.direction == 0 or self.snake.direction == 1:
                self.snake.direction = 2
        if event.char == 's':
            if self.snake.direction == 0 or self.snake.direction == 1:
                self.snake.direction = 3
        if event.char == 'd':
            if self.snake.direction == 2 or self.snake.direction == 3:
                self.snake.direction = 0
        if event.char == 'a':
            if self.snake.direction == 2 or self.snake.direction == 3:
                self.snake.direction = 1
        time.sleep(self.period)

    def listenKeyboard(self):
        self.entry.bind('<Key>', self.changedirection)
        self.entry.pack()

    def move(self):
        while True:
            self.has_new_food = False
            self.snake.move()
            if self.snake.snake_coord[0] == self.food.coord:
                self.snake.eat()
                self.food.generate(self.snake.snake_coord)
                self.has_new_food = True
            time.sleep(self.period)

    def getCurrentStatus(self):
        # snake information and food information
        return (self.food.coord, self.snake.snake_coord, self.snake.direction)


if __name__ == '__main__':
    print "Start Game"
    background = Background()
    background.draw()

    game = SnakeGame(background)
    game.init_game()
    game.background.root.mainloop()
